import airflow.models
from airflow.version import version as AIRFLOW_VERSION

from pkg_resources import parse_version

if parse_version(AIRFLOW_VERSION) >= parse_version("1.10.11"):
    from airflow import LoggingMixin
else:
    # Corrects path of import for Airflow versions below 1.10.11
    from airflow.utils.log.logging_mixin import LoggingMixin


class DAG(airflow.models.DAG, LoggingMixin):
    def __init__(self, *args, **kwargs):
        self.log.debug("odd dag starting")
        super().__init__(*args, **kwargs)

    def create_dagrun(self, *args, **kwargs):
        # run Airflow's create_dagrun() first
        self.log.debug(f"create_dagrun({args}, {kwargs})")
        dagrun = super(DAG, self).create_dagrun(*args, **kwargs)

        #create_dag_start_ms = self._now_ms()
        try:
            # send dagrun to ingestion
            self._send_dagrun(dagrun)
        except Exception as e:
            self.log.error(
                f'Failed to record metadata: {e} '
                f'{self._timed_log_message(create_dag_start_ms)}',
                exc_info=True
            )

        return dagrun

    def handle_callback(self, *args, **kwargs):
        self.log.debug(f"handle_callback({args}, {kwargs})")
        try:
            dagrun = args[0]
            self.log.debug(f"handle_callback() dagrun : {dagrun}")
            print("HERE! handle_callback")
            # self._report_task_instances(
            #     dagrun,
            #     kwargs.get('session')
            # )
        except Exception as e:
            self.log.error(
                f'Failed to record dagrun callback: {e} '
                f'dag_id={self.dag_id}',
                exc_info=True
            )

        return super().handle_callback(*args)

    def _send_dagrun(self, dagrun):
        # Собираем и валидируем данные
        print("VALIDATION")
        # Конвертим их в нужный формат (см. одд спеку)
        print("CONVERTION")
        # Отсылаем на ingest через try/except
        print("SEND TO INGESTION")
