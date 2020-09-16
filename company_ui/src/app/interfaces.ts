export interface Employee {
    id: number,
    last_login: Date,
    first_name: string,
    last_name: string,
    email: string,
    date_joined: Date    
}


export interface User {
    
}

export class Token {
    access: string;
    refresh: string;
}