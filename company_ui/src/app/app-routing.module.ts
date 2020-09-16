import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AuthGuard } from './helpers/auth.guard';
import { LoginComponent } from './login/login.component';
import { AppComponent } from './app.component';
import { EmployeeComponent } from './employee/employee.component';

const routes: Routes = [
  { path: '', component: EmployeeComponent, canActivate: [AuthGuard] },
  { path: 'login', component: LoginComponent },  

  // otherwise redirect to home
  { path: '**', redirectTo: 'login' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
