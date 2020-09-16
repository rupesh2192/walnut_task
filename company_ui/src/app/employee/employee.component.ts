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
  next = 0;
  previous = 0;
  constructor(private employee_service:EmployeeService) { }

  ngOnInit(): void {
    this.list_employees();
  }

  private list_employees(page=1){
    this.employee_service.list(page)
    .pipe(first())
    .subscribe(employees => {
      this.employees=employees.results;
      if (employees.next){
        this.next = employees.next.split("=")[1];
      }
      if (employees.previous){
        this.previous = employees.previous.split("=")[1] || 1;
      }      
    });
  }

  onNext(){
    this.list_employees(this.next);
    this.next = null;
  }

  onPrevious(){
    this.list_employees(this.previous);
    this.previous = null;
  }

}
