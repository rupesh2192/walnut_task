import { Component, OnInit } from '@angular/core';
import { EmployeeService } from '../services'
import { first } from 'rxjs/operators';
@Component({
  selector: 'app-employee',
  templateUrl: './employee.component.html',
  styleUrls: ['./employee.component.css']
})
export class EmployeeComponent implements OnInit {
  employees = [];
  constructor(private employee_service:EmployeeService) { }

  ngOnInit(): void {
    this.list_employees();
  }

  private list_employees(){
    this.employee_service.list()
    .pipe(first())
    .subscribe(employees => this.employees=employees.results);
  }

}
