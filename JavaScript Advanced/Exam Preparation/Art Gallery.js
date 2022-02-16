
class ArtGallery {
    constructor(creator) {
        this.creator = creator;
        this.possibleArticles = { "picture": 200, "photo": 50, "item": 250 }
        this.listOfArticles = [];
        this.guests = [];
        this.foundArticleName = false;
        this.guestFound = false;
        this.foundArticleModel = false;
    }

    addArticle(articleModel, articleName, quantity) {
    

        if (!Object.keys(this.possibleArticles).includes(articleModel.toLowerCase())) {
            throw new Error("This article model is not included in this gallery!");
        }

        for (let el of this.listOfArticles) {
            if (el["articleName"] == articleName) {
                el["quantity"] += Number(quantity);
                this.foundArticleName = true;

            }}
         
        if (!this.foundArticleName){
                this.listOfArticles.push({ articleModel: articleModel.toLowerCase(), articleName, quantity });
        }
        this.foundArticleName = false

         
        return `Successfully added article ${articleName} with a new quantity- ${quantity}.`

    }

    inviteGuest(guestName, personality){
        let points = 50;
        if(personality == "Vip"){
            points = 500;
        } else if(personality == "Middle"){
            points = 250;
        }

        for(let el of this.guests){
            if(el["guestName"]== guestName){
                this.guestFound = true;
                throw new Error(`${guestName} has already been invited.`)
        }}
        if(!this.guestFound){
            this.guests.push({guestName, points, purchaseArticle: 0})
        }
        this.guestFound = false

        return `You have successfully invited ${guestName}!`
    }
    

    buyArticle(articleModel, articleName, guestName){
        let currentArticleModelPrice = this.possibleArticles[articleModel];
        let currentPoints = 0;

        for (let el of this.listOfArticles){
            if(el["articleName"] == articleName){
                if(el["quantity"] < 1){
                    return `The ${articleName} is not available.`;
                }
                this.foundArticleName = true;

                if(el["articleModel"] != articleModel){
                    throw new Error("This article is not found.");
                }
                
        }}

        if(!this.foundArticleName){
            throw new Error("This article is not found.");
        }

        for (let g of this.guests){
            if(g["guestName"] == guestName){
                this.guestFound = true;
                currentPoints = g["points"];
                break
            }
        }
        if(!this.guestFound){
            return "This guest is not invited."
        } else{
            if(currentPoints < currentArticleModelPrice){
                return "You need to more points to purchase the article."
            } else{
                for (let g of this.guests){
                    if(g["guestName"] == guestName){
                        g.points -= Number(currentArticleModelPrice);
                        g["purchaseArticle"] += 1;
                    }
                }
                for (let el of this.listOfArticles){
                    if(el["articleName"] == articleName){
                        el.quantity -= 1;
                        break
                    }
                }
            }
            }

        this.guestFound = false;
        this.foundArticleModel = false;
        this.foundArticleName = false;

        return `${guestName} successfully purchased the article worth ${currentArticleModelPrice} points.`
    
    }
    

    showGalleryInfo(criteria){
        let result = "";
        if(criteria == "article"){
            result += "Articles information:" + "\n";
            for(let el of this.listOfArticles){
                result += `${el["articleModel"]} - ${el["articleName"]} - ${el["quantity"]}` + "\n";
            }
        } else if(criteria == "guest"){
            result += "Guests information:" + "\n";
            for(let g of this.guests){
                result += `${g["guestName"]} - ${g["purchaseArticle"]}` + "\n";
            }
        }
        return result.trimEnd();

        }
    } 



const artGallery = new ArtGallery('Curtis Mayfield');
artGallery.addArticle('picture', 'Mona Liza', 3);
artGallery.addArticle('Item', 'Ancient vase', 2);
artGallery.addArticle('PICTURE', 'Mona Liza', 1);
artGallery.inviteGuest('John', 'Vip');
artGallery.inviteGuest('Peter', 'Middle');
//console.log(artGallery.inviteGuest('John', 'Middle'));
console.log(artGallery.buyArticle('picture', 'Mona Liza', 'John'));
console.log(artGallery.buyArticle('item', 'Ancient vase', 'Peter'));
//console.log(artGallery.buyArticle('item', 'Mona Liza', 'John'));
console.log(artGallery.showGalleryInfo('article'));
console.log(artGallery.showGalleryInfo('guest'));
