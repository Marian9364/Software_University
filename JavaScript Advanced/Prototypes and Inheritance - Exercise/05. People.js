function solution(){
    class Employee{
        constructor(name, age){
            this.name = name;
            this.age = age;
            this.salary = 0;
            this.tasks = [];
        }
        work() {
            let currentTask = this.tasks.shift();
            this.tasks.push(currentTask);
            console.log(currentTask)
        };
        collectSalary(){
            console.log(`${this.name} received ${this.dividend ? (this.salary + this.dividend) : this.salary} this month.`)
        }
    }
    class Junior extends Employee{
        constructor(name, age){
            super(name, age);
            this.tasks.push(`${this.name} is working on a simple task.`)
        }
    }
    class Senior extends Employee{
        constructor(name, age){
            super(name, age);
            this.tasks.push(`${this.name} is working on a complicated task.`)
            this.tasks.push(`${this.name} is taking time off work.`)
            this.tasks.push(`${this.name} is supervising junior workers.`)
        }
    }
    class Manager extends Employee{
        constructor(name, age){
            super(name, age);
            this.dividend = 0;
            this.tasks.push(`${this.name} scheduled a meeting.`)
            this.tasks.push(`${this.name} is preparing a quarterly report.`)
        }
    }
    return {
        Employee,
        Junior,
        Senior,
        Manager
    }
}
