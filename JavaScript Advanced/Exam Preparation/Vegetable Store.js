class VegetableStore{
    constructor(owner, location){
        this.owner = owner;
        this.location = location;
        this.availableProducts = [];
    }

    loadingVegetables(vegetables){
        let foundProduct = "";
        let allTypes = [];

        for(let veg of vegetables){
            let [type, quantity, price] = veg.split(" ");

            quantity = Number(quantity);
            price = Number(price);

            if(this.availableProducts.find(x => x.type == type)){
                foundProduct = this.availableProducts.find(x=> x.type == type);
                if(foundProduct.price < price){
                    foundProduct.price = price;
                };
                foundProduct.quantity += quantity;
            } else{
                this.availableProducts.push({type, quantity, price})
            }
        }
        
        this.availableProducts.forEach(x => allTypes.push(x.type));
        return `Successfully added ${allTypes.join(", ")}`;
    }

    buyingVegetables (selectedProducts){
        let foundProduct = "";
        let totalPrice = 0.00;
        let currentPrice = 0;
        for (let prod of selectedProducts){
            let [type, quantity] = prod.split(" ");
            quantity = Number(quantity);

            foundProduct = this.availableProducts.find(x => x.type == type);
            if(!foundProduct){
                throw new Error(`${type} is not available in the store, your current bill is $${totalPrice.toFixed(2)}.`)
            }
            if(quantity > foundProduct.quantity){
                throw new Error(`The quantity ${quantity} for the vegetable ${type} is not available in the store, your current bill is $${totalPrice.toFixed(2)}.`)
            }

            currentPrice = foundProduct.price * quantity;
            foundProduct.quantity -= quantity;
            totalPrice += currentPrice;

        }
        return `Great choice! You must pay the following amount $${totalPrice.toFixed(2)}.`
    }

    rottingVegetable (type, quantity){
        let foundProduct = "";
        foundProduct = this.availableProducts.find(x => x.type == type);
        if(!foundProduct){
            throw new Error(`${type} is not available in the store.`)
        }
        if(foundProduct.quantity < quantity){
            foundProduct.quantity = 0;
            return `The entire quantity of the ${type} has been removed.`
        }
        foundProduct.quantity -= quantity;
        return `Some quantity of the ${type} has been removed.`

    }
    revision(){
        let result = "Available vegetables:" + "\n";
        let sortedProducts = this.availableProducts.sort((a,b) => a.price - b.price);
        sortedProducts.forEach(x => result += `${x.type}-${x.quantity}-$${x.price}` + "\n");
        result += `The owner of the store is ${this.owner}, and the location is ${this.location}.`
        return result
    }
}

// let vegStore = new VegetableStore("Jerrie Munro", "1463 Pette Kyosheta, Sofia");
// console.log(vegStore.loadingVegetables(["Okra 2.5 3.5", "Beans 10 2.8", "Celery 5.5 2.2", "Celery 0.5 2.5"]));
// console.log(vegStore.rottingVegetable("Okra", 1));
// console.log(vegStore.rottingVegetable("Okra", 2.5));
// console.log(vegStore.buyingVegetables(["Beans 8", "Celery 1.5"]));
// console.log(vegStore.revision());
