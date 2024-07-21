
# Temporary in-memory dictionary db with instances and without locking
# TODO: move to SQLite tables, add vector capabilities, etc.

# db = {
#     "assistants": {},
#     "messages": {},
#     "runs": {},
#     "file_objects": {},
#     "fine_tuning_jobs": {},
#     "fine_tuning_job_events": {},
#     "models": {},
#     "threads": {},
# }

# print('db: ', db)

# async_connector = SqlAlchemyConnector(
#     connection_info=ConnectionComponents(
#         driver=AsyncDriver.SQLITE_AIOSQLITE,
#         database="assistants.db"
#     )
# )

# connector = SqlAlchemyConnector(
#     connection_info=ConnectionComponents(
#         driver=SyncDriver.SQLITE_PYSQLITE,
#         database="assistants.db"
#     )
# )


class BorgSingleton(object):
  _shared_borg_state = {
      "assistants": {},
      "messages": {},
      "runs": {},
      "file_objects": {},
      "fine_tuning_jobs": {},
      "fine_tuning_job_events": {},
      "models": {},
      "threads": {},
  }
   
  def __new__(cls, *args, **kwargs):
    obj = super(BorgSingleton, cls).__new__(cls, *args, **kwargs)
    obj.__dict__ = cls._shared_borg_state
    return obj
   
borg = BorgSingleton()
borg.shared_variable = "Shared Variable"
