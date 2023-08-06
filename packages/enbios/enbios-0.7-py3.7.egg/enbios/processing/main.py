import os

import itertools
import tempfile

import pandas as pd
from typing import Tuple

from nexinfosys.common.decorators import deprecated
from nexinfosys.common.helper import download_file
from nexinfosys.embedded_nis import NIS
from nexinfosys.models.musiasem_concepts import Processor
from nexinfosys.serialization import deserialize_state

from enbios.common.helper import generate_workbook, hash_array, prepare_base_state, list_to_dataframe
from enbios.input import Simulation
from enbios.input.lci import LCIIndex
from enbios.input.simulators.calliope import CalliopeSimulation
from enbios.input.simulators.sentinel import SentinelSimulation
from enbios.processing import read_parse_configuration, read_submit_solve_nis_file
from enbios.processing.model_merger import Matcher, merge_models


#####################################################
# MAIN ENTRY POINT  #################################
#####################################################
class Enviro:
    def __init__(self):
        self._cfg_file_path = None
        self._cfg = None

    def set_cfg_file_path(self, cfg_file_path):
        self._cfg = read_parse_configuration(cfg_file_path)
        self._cfg_file_path = cfg_file_path if isinstance(cfg_file_path, str) else None

    def _prepare_base(self, solve: bool):
        """

        :return:
        """
        return prepare_base_state(self._cfg["nis_file_location"], solve)

    def _get_simulation(self) -> Simulation:
        # Simulation
        if self._cfg["simulation_type"].lower() == "calliope":
            simulation = CalliopeSimulation(self._cfg["simulation_files_path"])
        elif self._cfg["simulation_type"].lower() == "sentinel":
            simulation = SentinelSimulation(self._cfg["simulation_files_path"])
        return simulation

    def _prepare_process(self) -> Tuple[NIS, LCIIndex, Simulation]:
        # Simulation
        simulation = self._get_simulation()
        # MuSIASEM (NIS)
        nis = read_submit_solve_nis_file(self._cfg["nis_file_location"], state=None, solve=False)
        # LCI index
        lci_data_index = LCIIndex(self._cfg["lci_data_locations"])

        return nis, lci_data_index, simulation

    def generate_matcher_templates(self, combine_countries=False) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        """
        Generate auxiliary DataFrames to help in the elaboration of:
          - correspondence file
          - block types file
        :param combine_countries:
        :return: A tuple with 4 pd.DataFrames
        """
        # Construct auxiliary models
        nis, lci_data_index, simulation = self._prepare_process()
        # TODO Build a DataFrame with a list of LCI title, to file code
        #   name,title,file
        lci_df = pd.DataFrame()
        # TODO Build a DataFrame with a list of BareProcessors
        #   processor,parent
        nis_df = pd.DataFrame()
        # TODO Build DataFrame "correspondence"
        #   name,match_target_type,match_target,weight,match_conditions
        #   OK   "lca"             ---          1      <generate>
        #  if combine_countries:
        #   for each <name> generate a line per country and a line without country
        correspondence_df = pd.DataFrame()
        # TODO Build DataFrame "block_types"
        #   name,type
        #   OK   <from an existing database of tech names to Calliope tech types>
        block_types_df = pd.DataFrame()
        return lci_df, nis_df, correspondence_df, block_types_df

    def _read_simulation_fragments(self, split_by_region=True, split_by_scenario=True, split_by_period=True):

        """
        Read simulation. Find fragments and then start an iteration on them
        Each fragment is made of the "processors" and their "interfaces"
        It is here where basic processors are built. Correspondence file has tech but it could also
        have carrier and region

        :return:
        """
        # Create simulation
        simulation = self._get_simulation()
        # Read Simulation, returning:
        # prd: PartialRetrievalDictionary
        # scenarios: list of scenarios
        # regions: list of regions
        # times: list of time periods
        # carriers: list of carriers
        # col_types: list of value (not index) fields
        # ct: list of pairs (tech, region)
        prd, scenarios, regions, times, techs, carriers, col_types, ct = simulation.read("")

        partition_lists = []
        if split_by_region and len(regions) > 0:
            partition_lists.append([("_g", r) for r in regions])
        if split_by_period and len(times) > 0:
            partition_lists.append([("_d", t) for t in times])
        if split_by_scenario and len(scenarios) > 0:
            partition_lists.append([("_s", s) for s in scenarios])

        for partition in list(itertools.product(*partition_lists)):
            partial_key = {t[0]: t[1] for t in partition}
            procs = prd.get(partial_key)
            # TODO Sweep "procs" and update periods, regions, scenarios, models and carriers
            md = dict(periods=[], regions=[], scenarios=[], models=[], carriers=[])
            yield partial_key, md, procs

    def compute_indicators_from_base_and_simulation(self):
        """
        MAIN entry point of current ENVIRO
        Previously, a Base NIS must have been prepared, see @_prepare_base

        :return:
        """
        # Prepare Base
        serial_state = self._prepare_base(solve=False)
        output_dir = tempfile.gettempdir()
        # Split in fragments, process each fragment separately
        # Acumulate results
        indicators = pd.DataFrame()
        for partial_key, fragment_metadata, fragment_processors in self._read_simulation_fragments():
            # fragment_metadata: dict with regions, years, scenarios in the fragment
            # fragment_processors: list of processors with their attributes which will be interfaces
            print(f"{partial_key}: {len(fragment_processors)}")
            results = process_fragment(serial_state, partial_key, fragment_metadata, fragment_processors, output_dir)

            # TODO Append "results" to "indicators"
            indicators += results

        # TODO Save indicators DataFrame as a single CSV file

    @deprecated  # Use "compute_indicators_from_base_and_simulation"
    def musiasem_indicators(self, system_per_country=True):
        """
        From the configuration file, read all inputs
          - Base NIS format file
          - Correspondence file
          - Simulation type, simulation location
          - LCI databases

        :param system_per_country:
        :return:
        """
        # Construct auxiliary models
        nis, lci_data_index, simulation = self._prepare_process()
        # Matcher
        matcher = Matcher(self._cfg["correspondence_files_path"])

        # ELABORATE MERGE NIS FILE
        lst = merge_models(nis, matcher, simulation, lci_data_index)

        # Generate NIS file into a temporary file
        temp_name = tempfile.NamedTemporaryFile(dir=self._cfg["output_directory"], delete=False)
        s = generate_workbook(lst)
        if s:
            with open(temp_name, "wb") as f:
                f.write(s)
        else:
            print(f"ACHTUNG BITTE!: it was not possible to produce XLSX")

        # Execute the NIS file
        nis, issues = read_submit_solve_nis_file(temp_name)

        # TODO Download outputs
        # TODO Elaborate indicators
        # TODO Write indicator files

        # os.remove(temp_name)


def process_fragment(base_serial_state, partial_key, fragment_metadata, fragment_processors, output_directory):
    state = deserialize_state(base_serial_state)
    prd = state.get("_glb_idx")
    procs = prd.get(Processor.partial_key())
    base_musiasem_procs = {}
    structural_lci_procs = {}
    for proc in procs:
        n_interfaces = len(proc.factors)
        accounted = proc.instance_or_archetype.lower() == "instance"
        functional = proc.functional_or_structural.lower() == "functional"
        if functional and accounted and n_interfaces == 0:
            for hname in proc.full_hierarchy_names(prd):
                base_musiasem_procs[hname] = proc
        elif not functional and not accounted and n_interfaces > 0:
            for hname in proc.full_hierarchy_names(prd):
                structural_lci_procs[hname] = proc
        else:
            print(f"{proc.full_hierarchy_names(prd)[0]} is neither MuSIASEM base nor LCI base "
                  f"(functional: {functional}; accounted: {accounted}; n_interfaces: {n_interfaces}.")

    processors = [
        ["ProcessorGroup", "Processor", "ParentProcessor", "SubsystemType", "System", "FunctionalOrStructural",
         "Accounted", "Stock", "Description", "GeolocationRef", "GeolocationCode", "GeolocationLatLong", "Attributes",
         "@SimulationName", "@Region"]]  # TODO Maybe more fields to qualify the fragment
    interfaces = [
        ["Processor", "InterfaceType", "Interface", "Sphere", "RoegenType", "Orientation", "OppositeSubsystemType",
         "GeolocationRef", "GeolocationCode", "InterfaceAttributes", "Value", "Unit", "RelativeTo", "Uncertainty",
         "Assessment", "PedigreeMatrix", "Pedigree", "Time", "Source", "NumberAttributes", "Comments"]]
    clone = False
    if clone:
        cloners = [
            ["InvokingProcessor", "RequestedProcessor", "ScalingType", "InvokingInterface", "RequestedInterface",
             "Scale"]]
        clone_processors = [
            ["ProcessorGroup", "Processor", "ParentProcessor", "SubsystemType", "System", "FunctionalOrStructural",
             "Accounted", "Stock", "Description", "GeolocationRef", "GeolocationCode", "GeolocationLatLong",
             "Attributes",
             "@SimulationName", "@Region"]]
        # TODO Find regions in the fragment
        #  for each region, create a processor in "clone_processors" and an entry in "cloners" hanging the top Processor into the top processor
        regions = []
        for r in regions:
            name = None
            clone_processors.append(["", name, "", "", "<system>", "Functional", "Yes", "",
                                     f"Country level processor, {t[1]}", "", "", "", "", t[1], t[1]])
            # TODO InvokingInterface, RequestedInterface, Scale are mandatory; specify something here
            cloners.append((name, "EnergySector", "Clone", "", "", ""))
    already_added_processors = set()
    for p in fragment_processors:
        # TODO Update time and scenario (can change from entry to entry, but for MuSIASEM it would be the same entity)
        time_ = None
        scenario = None
        # TODO Find MuSIASEM matches
        musiasem_matches = []  # find_musiasem_parents(p)
        first_name = None
        for m in musiasem_matches:
            name = None
            parent = None
            description = None
            original_name = None
            if first_name is None:
                first_name = ""
                if (name, parent) not in already_added_processors:
                    processors.append(["", name, parent, "", "system", "Structural", "Yes", "",
                                       description, "", "", "", "", original_name, t[1]])
                    already_added_processors.add((name, parent))
            else:
                if (name, parent) not in already_added_processors:
                    processors.append(["", name, parent, "", "system", "Structural", "Yes", "",
                                       "", "", "", "", "", "", ""])
                    already_added_processors.add((name, parent))

        if first_name is not None:
            for i in p.ifaces:
                interfaces.append([name, i, "", "Technosphere", "Flow", "<orientation>", "", "", "", "", v,
                                   "", "<relative_to>", "", "", "", "", time_, scenario, "", ""])

            lci_matches = []  # find_lci_matches(p)
            # TODO Find LCI matches, expand interfaces
            for cp in lci_matches:
                for i in cp.ifaces:
                    orientation = "Input"
                    v = 1  # TODO Value
                    relative_to = "flow_out"
                    interfaces.append([first_name, i, "", "", "", orientation, "", "", "", "", v,
                                       "", relative_to, "", "", "", "", time_, scenario, "", ""])

    # Generate NIS file
    cmds = []
    if clone:
        cmds.append(("BareProcessors regions", list_to_dataframe(clone_processors)))
        cmds.append(("ProcessorScalings", list_to_dataframe(cloners)))
    cmds.append(("BareProcessors simulation fragment", list_to_dataframe(processors)))
    cmds.append(("Interfaces simulation fragment", list_to_dataframe(interfaces)))
    s = generate_workbook(cmds)
    if s:
        temp_name = tempfile.NamedTemporaryFile(dir=output_directory, delete=False)
        with open(temp_name, "wb") as f:
            f.write(s)

        nis = NIS()
        nis.open_session(True, state)
        nis.load_workbook(temp_name)
        r = nis.submit_and_solve()
        tmp = nis.query_available_datasets()
        print(tmp)
        # TODO Obtain indicators matrix:
        #   (scenario, processor, region, time, ¿carrier?) -> (i1, ..., in)
        # TODO Append to global indicators matrix (this could be done sending results and another process
        #  would be in charge of assembling)
        nis.close_session()
        return None  # TODO Return a pd.DataFrame
    else:
        return pd.DataFrame()


if __name__ == '__main__':
    t = Enviro()
    _ = dict(nis_file_location="https://docs.google.com/spreadsheets/d/15NNoP8VjC2jlhktT0A8Y0ljqOoTzgar8l42E5-IRD90/edit#gid=839302943",
             correspondence_files_path="",
             simulation_type="sentinel",
             simulation_files_path="/home/rnebot/Downloads/borrame/calliope-output/datapackage.json",
             lci_data_locations={},
             output_directory="/home/rnebot/Downloads/borrame/enviro-output/")
    t.set_cfg_file_path(_)
    t.compute_indicators_from_base_and_simulation()
    print("Done")


