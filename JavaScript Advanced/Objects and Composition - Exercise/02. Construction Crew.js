function constructionCrew(worker){

    if(worker['dizziness'] == true){
        worker['levelOfHydrated'] += Number(0.1 * worker['weight']);
    }
    worker['dizziness'] = false;
    
    return worker;
}
