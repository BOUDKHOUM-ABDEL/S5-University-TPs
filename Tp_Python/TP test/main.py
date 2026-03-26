import os
import shutil
from datetime import datetime
from exceptions import EmployeeNotFoundError, InvalidDepartmentError, InvalidSalaryError, FileBackupError

def load_employees(path):
    lst = []
    try:
        f = open(path, "r", encoding="utf-8")
        for line in f:
            try:
                p = line.strip().split(";")
                if len(p) != 4:
                    raise ValueError()
                x = {
                    "id": int(p[0]),
                    "name": p[1],
                    "department": p[2],
                    "salary": float(p[3])
                }
                lst.append(x)
            except:
                continue
        f.close()
        return lst
    except:
        return []

def load_departments(path):
    lst = []
    try:
        f = open(path, "r", encoding="utf-8")
        for line in f:
            s = line.strip()
            if not s.isalpha():
                raise ValueError()
            lst.append(s)
        f.close()
        if len(lst) == 0:
            raise ValueError()
        return lst
    except:
        return []

def find_employee_by_id(lst, x):
    try:
        x = int(x)
    except:
        return None
    for e in lst:
        if e["id"] == x:
            return e
    return None

def filter_by_department(lst, d):
    r = []
    for e in lst:
        if e["department"] == d:
            r.append(e)
    return r

class EmployeeManager:
    def __init__(self, employees, departments):
        self.employees = employees
        self.departments = departments

    def add_employee(self, i, n, d, s):
        if d not in self.departments:
            raise InvalidDepartmentError("invalid department")
        try:
            i = int(i)
            s = float(s)
        except:
            raise InvalidSalaryError("invalid salary")
        for e in self.employees:
            if e["id"] == i:
                raise EmployeeError("id used")
        self.employees.append({"id": i, "name": n, "department": d, "salary": s})

    def remove_employee(self, i):
        try:
            i = int(i)
        except:
            raise EmployeeNotFoundError("not found")
        for e in self.employees:
            if e["id"] == i:
                self.employees.remove(e)
                return
        raise EmployeeNotFoundError("not found")

    def update_salary(self, i, s):
        try:
            i = int(i)
            s = float(s)
        except:
            raise InvalidSalaryError("invalid salary")
        for e in self.employees:
            if e["id"] == i:
                e["salary"] = s
                return
        raise EmployeeNotFoundError("not found")

    def save_to_file(self, path):
        try:
            f = open(path, "w", encoding="utf-8")
            for e in self.employees:
                f.write(f"{e['id']};{e['name']};{e['department']};{e['salary']}\n")
            f.close()
        except:
            pass

def backup_file(src, folder):
    try:
        if not os.path.exists(folder):
            os.makedirs(folder)
        t = datetime.now().strftime("%Y%m%d_%H%M")
        dest = os.path.join(folder, f"employees_backup_{t}.txt")
        shutil.copy(src, dest)
        return dest
    except:
        raise FileBackupError("backup failed")

def export_csv(lst, path):
    try:
        f = open(path, "w", encoding="utf-8")
        f.write("id,name,department,salary\n")
        for e in lst:
            f.write(f"{e['id']},{e['name']},{e['department']},{e['salary']}\n")
        f.close()
    except:
        pass

def export_json(lst, path):
    try:
        f = open(path, "w", encoding="utf-8")
        f.write('{\n  "employees": [\n')
        for i, e in enumerate(lst):
            f.write("    {\n")
            f.write(f'      "id": {e["id"]},\n')
            f.write(f'      "name": "{e["name"]}",\n')
            f.write(f'      "department": "{e["department"]}",\n')
            f.write(f'      "salary": {e["salary"]}\n')
            if i == len(lst) - 1:
                f.write("    }\n")
            else:
                f.write("    },\n")
        f.write("  ]\n}")
        f.close()
    except:
        pass

if __name__ == "__main__":
    emp = load_employees("employees.txt")
    dep = load_departments("departments.txt")
    m = EmployeeManager(emp, dep)

    m.save_to_file("employees.txt")
    backup_file("employees.txt", "backups")
    export_csv(emp, "export.csv")
    export_json(emp, "export.json")
