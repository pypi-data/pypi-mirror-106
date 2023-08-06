from coopui.cli.CliAtomicUserInteraction import CliAtomicUserInteraction
from coopgantt.build_and_schedule_gantt import build_and_schedule
from coopgantt import build_html, build_svgs, Resource

class UserOperations:
    def __init__(self, user_interaction: CliAtomicUserInteraction):
        self.ui = user_interaction
        self.gantt = None
        self.gantt_name = ""
        self.task_filepath = None
        self.resources_filepath = None
        self.html_output_path = None
        self.svg_renderings_dir = None
        self.out_file = None

    def generate_a_gantt(self, task_filepath: str = None, resources_filepath: str = None, gantt_name: str = None):

        # Get name
        if gantt_name is None:
            gantt_name = self.ui.request_string("Gantt Name:")
        if gantt_name is None: return

        # Get task data
        task_columns = {
            'id': int,
            'project': str,
            'activity_type': str,
            'activity': str,
            'actual_start_date': str,
            'duration_days': int,
            'resources': str,
            'perc_done': int,
            'dependencies': str,
            'priority': int,
            'state': str,
            'sub_activities': str,
            'target_completion_date': str,
            'closed_date': str,
            'scheduled_start_date': str,
            'dont_start_before_date': str
        }

        task_data = self.ui.request_data_from_csv_with_specified_columns(task_columns, title="Gantt Activities", filepath=task_filepath)
        if task_data is None: return

        task_data = task_data.fillna('')
        task_data = task_data.replace('nan', '')

        # Get resources data
        resources_columns = {
            'resource': str,
            'capacity': int
        }
        resources = self.ui.request_data_from_csv_with_specified_columns(resources_columns, title="Resources", filepath=resources_filepath)
        if resources is None: return
        resources = resources.fillna('')

        resources = [Resource(resource['resource'], capacity=resource['capacity']) for resource in resources.to_dict('records')]

        # Build
        self.ui.notify_user(text="Building Gantt...")
        self.gantt = build_and_schedule(gantt_name=gantt_name,
                                   gantt_task_data=task_data.to_dict('records'),
                                   resources=resources,
                                   # resource_max_by_project=resource_maxes.to_dict('records')
                                   )

        print(self.gantt)

    def render_an_html(self, html_output_path: str = None, svg_renderings_dir: str = None):

        if self.gantt is None or any(self.gantt.activities_not_scheduled):
            self.ui.notify_user("Gantt must be generated before rendering")
            return None

        if html_output_path is None:
            html_output_path = self.ui.request_save_filepath(prompt="Select a path to save the HTML")
        if html_output_path is None: return None

        if svg_renderings_dir is None:
            svg_renderings_dir = self.ui.request_directory(prompt="Select a path to save the .svg files")
        if svg_renderings_dir is None: return None

        build_svgs(self.gantt, output_dirs=[svg_renderings_dir])
        build_html(self.gantt, svg_input_dir=svg_renderings_dir, embed_css=True, output_dirs=[html_output_path])

    def generate_gantt_task_data(self):
        task_save_file = self.ui.request_save_filepath(prompt="Select a path to save the Gantt task data")
        if task_save_file is None: return None

    def save_gantt_data(self, out_file: str = None):
        if self.gantt is None:
            self.ui.notify_user(f"Gantt project must be loaded before saving")
            return

        if out_file is None:
            out_file = self.ui.request_save_filepath("Choose a save file path", filetypes=(("CSV", ".csv"),))
        if out_file is None:
            return

        df = self.gantt.as_dataframe()
        df.to_csv(out_file, index=None)

    def set_state(self):
        self.task_filepath = self.ui.request_open_filepath(prompt="Task data filepath", filetypes=(("CSV", ".csv"),))
        if self.task_filepath is None: return None
        self.resources_filepath = self.ui.request_open_filepath(prompt="Resources data filepath", filetypes=(("CSV", ".csv"),))
        if self.resources_filepath is None: return None
        self.html_output_path = self.ui.request_save_filepath(prompt="Select a path to save the HTML")
        if self.html_output_path is None: return None
        self.svg_renderings_dir = self.ui.request_directory(prompt="Select a path to save the .svg files")
        if self.svg_renderings_dir is None: return None
        self.out_file = self.ui.request_save_filepath("Choose a save file path", filetypes=(("CSV", ".csv"),))
        if self.out_file is None: return None
        self.gantt_name = self.ui.request_string("Gantt Name: ")


    def create_render_and_save(self):

        if self.task_filepath is None or \
            self.resources_filepath is None or \
            self.html_output_path is None or \
            self.svg_renderings_dir is None or \
            self.out_file is None:
            self.ui.notify_user(text="Please set state before running")
            return None

        self.generate_a_gantt(self.task_filepath, self.resources_filepath, gantt_name=self.gantt_name)
        self.render_an_html(self.html_output_path, self.svg_renderings_dir)
        self.save_gantt_data(self.out_file)

