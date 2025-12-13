from Departments.Department import Department

class HR_department(Department):
    def __init__(self, square, interview_rooms, hr_specialists=None):
        super().__init__(square)
        self.interview_rooms = interview_rooms
        self._hr_specialists = hr_specialists or []

    def add_hr_specialist(self, hr):
        from Humans.HR import HR
        if isinstance(hr, HR):
            self._hr_specialists.append(hr)
            hr.set_department(self)
        else:
            print("Ошибка: добавлять можно только HR-специалистов")

    def get_hr_count(self):
        return len(self._hr_specialists)

    def list_hr_names(self):
        return [hr.name for hr in self._hr_specialists]

    def has_room_for_interview(self):
        return self.interview_rooms > 0