

describe("company administration test", ()=> {
    describe("hiring employee method testing", ()=>{
        it("should throw an error if position is not Programmer", ()=> {
            //arrange
            let expected = `We are not looking for workers for this position.`;
            //act
            
            //assert
            expect(()=>companyAdministration.hiringEmployee("Pesho", "A", 2)).to.throw(Error, expected);
        });
        it("should return string for successfully hired employee when years of experience are equal to 3", ()=> {
            //arrange
            let name = "Pesho";
            let position = "Programmer"
            let expected = `${name} was successfully hired for the position ${position}.`;
            //act
           
            //assert
            expect(companyAdministration.hiringEmployee("Pesho", "Programmer", 3)).to.equal(expected);
            expect(companyAdministration.hiringEmployee("Pesho", "Programmer", 4)).to.equal(expected);
        });
        it("should return string for successfully hired employee when years of experience are equal to 3", ()=> {
            //arrange
            let name = "Pesho";
            let expected = `${name} is not approved for this position.`;
            //act
           
            //assert
            expect(companyAdministration.hiringEmployee("Pesho", "Programmer", 2)).to.equal(expected);
            expect(companyAdministration.hiringEmployee("Pesho", "Programmer", 1)).to.equal(expected);
        });
     });
     describe("caclulate salary method testing", ()=>{
        it("should throw an error when hours is not a number or hours is negative number", ()=> {
            //arrange
            //act
            
            //assert
            expect(()=>companyAdministration.calculateSalary(-1)).to.throw("Invalid hours");
            expect(()=>companyAdministration.calculateSalary("1")).to.throw("Invalid hours");
            expect(()=>companyAdministration.calculateSalary([])).to.throw("Invalid hours");
            
        });
        it("should return salary when happy case", ()=> {
            //arrange
            //act
            //assert
            expect(companyAdministration.calculateSalary(3)).to.equal(45);
            expect(companyAdministration.calculateSalary(160)).to.equal(2400);
            expect(companyAdministration.calculateSalary(161)).to.equal(3415);
        });
        it("should return string for successfully hired employee when years of experience are equal to 3", ()=> {
            //arrange
            let name = "Pesho";
            let expected = `${name} is not approved for this position.`;
            //act
           
            //assert
            expect(companyAdministration.hiringEmployee("Pesho", "Programmer", 2)).to.equal(expected);
            expect(companyAdministration.hiringEmployee("Pesho", "Programmer", 1)).to.equal(expected);
        });
     });
     describe("fired employee method testing", ()=>{
        it("should throw an error when array of employees is not an array", ()=> {
            //arrange
            //act
            
            //assert
            expect(()=>companyAdministration.firedEmployee({}, 2)).to.throw("Invalid input");
            expect(()=>companyAdministration.firedEmployee(2, 2)).to.throw("Invalid input");
            expect(()=>companyAdministration.firedEmployee("3", 2)).to.throw("Invalid input");
            expect(()=>companyAdministration.firedEmployee("", 2)).to.throw("Invalid input");
         
            
        });
        it("should throw an error when index is not a number or out of range", ()=> {
            //arrange
            //act
            let arr = ["a", "b", "c"]
            //assert
            expect(()=>companyAdministration.firedEmployee(arr, 3)).to.throw("Invalid input");
            expect(()=>companyAdministration.firedEmployee(arr, -1)).to.throw("Invalid input");
            expect(()=>companyAdministration.firedEmployee(arr, "2")).to.throw("Invalid input");
            expect(()=>companyAdministration.firedEmployee(arr, "")).to.throw("Invalid input");
            
            
         
            
        });
        it("should remove an element of the array's index", ()=> {
            //arrange
            let arr = ["a", "b", "c"]
            //act
            //assert
            expect(companyAdministration.firedEmployee(arr, 0)).to.equal('b, c');
            expect(companyAdministration.firedEmployee(arr, 2)).to.equal('a, b');
          
        });

     }); 
       

});
