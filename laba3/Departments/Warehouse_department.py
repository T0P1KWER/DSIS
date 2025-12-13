from Departments.Department import Department

class Warehouse_department(Department):
    def __init__(self, square, storage_capacity, forklifts_count,count_of_shelf):
        super().__init__(square)
        self.storage_capacity = storage_capacity
        self.forklifts_count = forklifts_count
        self._workers = []
        self.__count_of_shelf=count_of_shelf


    def add_worker(self, worker):
        from Humans.Warehouse_worker import Warehouse_worker
        if isinstance(worker, Warehouse_worker):
            self._workers.append(worker)
        else:
            print("Ошибка: можно добавить только грузчика (Warehouse_worker)")

    def get_workers_count(self):
        return len(self._workers)

    def list_workers(self):
        return [w.name for w in self._workers]

    def is_full(self, current_items):
        return current_items >= self.storage_capacity

    def has_forklifts(self):
        return self.forklifts_count > 0