const flowerShop = require("./flowerShop");
const { expect } = require("chai");

describe("nameOfFile test", ()=> {
    describe("calcPriceOfFLowers method testing", ()=>{
        it("should throw an error when flower not a string", ()=> {
            //arrange
            let expected = "Invalid input!";
            //act
            
            //assert
            expect(()=>flowerShop.calcPriceOfFlowers(2, 2, 2)).to.throw(Error, expected);
            expect(()=>flowerShop.calcPriceOfFlowers([], 2, 2)).to.throw(Error, expected);
            expect(()=>flowerShop.calcPriceOfFlowers({}, 2, 2)).to.throw(Error, expected);
        });
        it("should throw an error when price not a number", ()=> {
            //arrange
            let expected = "Invalid input!";
            //act
            
            //assert
            expect(()=>flowerShop.calcPriceOfFlowers('minzuhar', "2", 2)).to.throw(Error, expected);
            expect(()=>flowerShop.calcPriceOfFlowers('minzuhar', [], 2)).to.throw(Error, expected);
            expect(()=>flowerShop.calcPriceOfFlowers('minzuhar', {}, 2)).to.throw(Error, expected);
 
        });
        it("should throw an error when quantity not a number", ()=> {
            //arrange
            let expected = "Invalid input!";
            //act
            
            //assert
            expect(()=>flowerShop.calcPriceOfFlowers('minzuhar', 2, "2")).to.throw(Error, expected);
            expect(()=>flowerShop.calcPriceOfFlowers('minzuhar', 2, [])).to.throw(Error, expected);
            expect(()=>flowerShop.calcPriceOfFlowers('minzuhar', 2, {})).to.throw(Error, expected);

 
        });
        it("should return string when happy case", ()=> {
            //arrange
            let flower = "minzuhar"
            let result = 2 * 2;
            // let position = "Programmer"
            let expected = `You need $${result.toFixed(2)} to buy ${flower}!`;
            //act
           
            //assert
            expect(flowerShop.calcPriceOfFlowers("minzuhar", 2, 2)).to.equal(expected);
            expect(flowerShop.calcPriceOfFlowers("minzuhar", 2.0, 2.0)).to.equal(expected);
            
            //expect(flowerShop.calcPriceOfFlowers("minzuhar", 3.2, 2.5)).to.equal("You need $8.00 to buy minzuhar!");
        });

     }); 
     describe("calcPriceOfFLowers method testing", ()=>{
        it("should check if gardenarr has flower if not return string purchase more", ()=> {
            //arrange
            let gardenArr = ["Rose", "Lily", "Orchid"];
            // let position = "Programmer"
            //let expected = `You need $${result.toFixed(2)} to buy ${flower}!`;
            //act
           
            //assert
            expect(flowerShop.checkFlowersAvailable("minzuhar", gardenArr)).to.equal(`The minzuhar are sold! You need to purchase more!`);
            //expect(flowerShop.checkFlowersAvailable("minzuhar", 2.0, 2.0)).to.equal(expected);
            
            //expect(flowerShop.calcPriceOfFlowers("minzuhar", 3.2, 2.5)).to.equal("You need $8.00 to buy minzuhar!");
        });
        it("should check if gardenarr has flower and return string ..are available", ()=> {
            //arrange
            let gardenArr = ["Rose", "Lily", "Orchid"];
            // let position = "Programmer"
            //let expected = `You need $${result.toFixed(2)} to buy ${flower}!`;
            //act
           
            //assert
            expect(flowerShop.checkFlowersAvailable("Rose", gardenArr)).to.equal(`The Rose are available!`);
            //expect(flowerShop.checkFlowersAvailable("minzuhar", 2.0, 2.0)).to.equal(expected);
            
            //expect(flowerShop.calcPriceOfFlowers("minzuhar", 3.2, 2.5)).to.equal("You need $8.00 to buy minzuhar!");
        });
    });
    describe("sellFlowers method testing", ()=>{
        it("should check if gardenarr has flower if not return string purchase more", ()=> {
            //arrange
            
            let gardenArr = ["Rose", "Lily", "Orchid"];
            // let position = "Programmer"
            //let expected = `You need $${result.toFixed(2)} to buy ${flower}!`;
            //act
           
            //assert
            expect(flowerShop.sellFlowers(gardenArr, 0)).to.equal('Lily / Orchid');
            expect(flowerShop.sellFlowers(gardenArr, 2)).to.equal('Rose / Lily');
            //expect(flowerShop.checkFlowersAvailable("minzuhar", 2.0, 2.0)).to.equal(expected);
            
            //expect(flowerShop.calcPriceOfFlowers("minzuhar", 3.2, 2.5)).to.equal("You need $8.00 to buy minzuhar!");
        });
        it("should throw an error when space index out of range", ()=> {
            //arrange
            let expected = "Invalid input!";
            let gardenArr = ["Rose", "Lily", "Orchid"];
            //act
            
            //assert
            expect(()=>flowerShop.calcPriceOfFlowers(-1, gardenArr)).to.throw(Error, expected);
            expect(()=>flowerShop.calcPriceOfFlowers(3, gardenArr)).to.throw(Error, expected);
            expect(()=>flowerShop.calcPriceOfFlowers(10,gardenArr)).to.throw(Error, expected);

 
        });

    });




   
       

});