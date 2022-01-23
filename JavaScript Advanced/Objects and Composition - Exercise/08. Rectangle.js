function rectangle(width, heigth, color){
 
    let patternRect = {
                    width,
                    heigth,
                    color,
                    calcArea(){
                        return(this.width * this.heigth)
                    }                  
    }
    let newColor = (patternRect.color[0]).toUpperCase() + patternRect.color.substring(1)
    patternRect.color = newColor
     
     
    return patternRect
     
    }
