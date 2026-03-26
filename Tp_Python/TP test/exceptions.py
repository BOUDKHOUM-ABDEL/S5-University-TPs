class EmployeeError(Exception):
    def __str__(self):
        return self.args[0]

class EmployeeNotFoundError(EmployeeError):
    pass

class InvalidDepartmentError(EmployeeError):
    pass

class InvalidSalaryError(EmployeeError):
    pass

class FileBackupError(EmployeeError):
    pass
