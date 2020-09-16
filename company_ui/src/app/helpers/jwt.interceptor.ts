import { Injectable } from '@angular/core';
import { HttpRequest, HttpHandler, HttpEvent, HttpInterceptor } from '@angular/common/http';
import { Observable } from 'rxjs';

import { AuthenticationService } from '../services';

@Injectable()
export class JwtInterceptor implements HttpInterceptor {
    constructor(private authenticationService: AuthenticationService) {}

    intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
        // add authorization header with jwt token if available        
        let currentUser = this.authenticationService.currentUserValue;
        if (currentUser && currentUser.access) {
            let new_request = request.clone({
                setHeaders: { 
                    Authorization: `Bearer ${currentUser.access}`
                }
            });
            return next.handle(new_request);
        }        
        return next.handle(request);
    }
}