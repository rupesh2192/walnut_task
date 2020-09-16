import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { Employee, User } from '../interfaces';
import { CONFIG } from './config';

const config = CONFIG;

@Injectable({ providedIn: 'root' })
export class EmployeeService {    

    constructor(private http: HttpClient) {        
    }
    
    list(page=1) {
        return this.http.get<any>(`${config.base_url}/api/employees?page=${page}`)
            .pipe(map(employees => {                                                
                return employees;
            }));
    }
}