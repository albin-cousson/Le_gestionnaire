let idea = document.querySelectorAll(".idea")
let card = document.querySelectorAll(".card")
let list_sous = document.querySelectorAll(".list-group")
let rienMain = document.querySelectorAll(".rienMain")
let rien = document.querySelectorAll(".rien")
let categorie = document.querySelectorAll(".categorie")
let main_categorie = document.querySelector(".main_categorie")
let sous_categorie = document.querySelectorAll(".sous_categorie")

//Apparition du menu "projet de vie" lors du clique sur le fleche
let projetVie__fleche = document.querySelector(".projetVie__fleche")
let projetVie__page = document.querySelector(".projetVie__page")

try {
    projetVie__fleche.addEventListener("click", () => {
    projetVie__page.parentNode.classList.add("projetVie__page__active")
    blockMainIdea.style.zIndex = "5"
    projetVie__page.style.zIndex = "10"
})
}catch {

}

//Dispparition du menu "projet de vie" lors du clique sur la flèche
let projetVie__page__close = document.querySelector(".projetVie__page__close")
let blockMainIdea = document.querySelector(".blockMainIdea")

try {
    projetVie__page__close.addEventListener("click", () => {
    projetVie__page.parentNode.classList.remove("projetVie__page__active")
    projetVie__page.style.zIndex = "6"
    setTimeout (function() {
        blockMainIdea.style.zIndex = "6"
        projetVie__page.style.zIndex = "5"
    }, 1000)
})
}catch{
    
}

//foction qui fait apparatitre le message de confiramtion pour supprimer une main__idea
let blockMainIdea__nav__item__buttonCroix = document.querySelectorAll(".blockMainIdea__nav__item__buttonCroix")
let blockSuppression__mainIdea = document.querySelectorAll(".blockSuppression__mainIdea")
let blockSuppression__mainIdea__non = document.querySelectorAll(".blockSuppression__mainIdea__non")
try {
    for (i=0; i<blockMainIdea__nav__item__buttonCroix.length; i++){
        blockMainIdea__nav__item__buttonCroix[i].addEventListener("click", function(){
            for (j=0; j<blockSuppression__mainIdea.length; j++) {
                let idConfirmation = this.id
                if (blockSuppression__mainIdea[j].id == idConfirmation) {
                    blockSuppression__mainIdea[j].style.display="flex"
                }
            }
        })
    }
}
catch{
    console.error("C'est réussi");
}
    //foction qui fait disparatitre le message de confirmation pour ne pas supprimer une main__idea
    try {
        for (i=0; i<blockMainIdea__nav__item__buttonCroix.length; i++){
            blockSuppression__mainIdea__non[i].addEventListener("click", function(){
                for (j=0; j<blockMainIdea__nav__item__buttonCroix.length; j++){
                    blockSuppression__mainIdea[j].style.display="none"
                }
            })
        }
    }
    catch{
        console.error("C'est réussi");
    }
//foction qui fait apparatitre le message de confiramtion pour supprimer une second__idea
let secondIdea__buttonCroix = document.querySelectorAll(".secondIdea__buttonCroix")
let secondIdea__buttonConfirmation = document.querySelectorAll(".secondIdea__buttonConfirmation")
let secondIdea__bouttonConfirmation__non = document.querySelectorAll(".secondIdea__bouttonConfirmation__non")
try {
    for (i=0; i<secondIdea__buttonCroix.length; i++){
        secondIdea__buttonCroix[i].addEventListener("click", function(){
            for (j=0; j<secondIdea__buttonConfirmation.length; j++){
                idConfirmation = this.id
                    if (secondIdea__buttonConfirmation[j].id == idConfirmation) {
                        secondIdea__buttonConfirmation[j].style.display="flex"
                    } 
            }
        })
    }
}
catch {
    console.error("C'est réussi");
}
    //foction qui fait disparatitre le message de confiramtion pour supprimer une second__idea
    try {
        for (i=0; i<secondIdea__bouttonConfirmation__non.length; i++){
            secondIdea__bouttonConfirmation__non[i].addEventListener("click", function(){
                for (j=0; j<secondIdea__buttonConfirmation.length; j++){
                    secondIdea__buttonConfirmation[j].style.display="none"
                }
            })
        }
    }
    catch{
        console.error("C'est réussi");
    }

//fonction qui fait disparaitre les poubelle des third__ideas du programme 
let list__group__item__programme__mainCategorie = document.querySelectorAll(".list-group-item__programme__mainCategorie")
let list__group__item__svg__poubelle = document.querySelectorAll(".list-group-item__svg__poubelle")
try {
    for (i=0; i<list__group__item__programme__mainCategorie.length; i++){
        if (list__group__item__programme__mainCategorie[i].textContent == "None"){
            list__group__item__svg__poubelle[i].style.display="none"
        }
    }
}
catch {
    console.error("C'est réussi");
}

//fonction qui fait apparaitre les seconde__ideas des third__ideas du programme 
let list__group__item__programme__idea = document.querySelectorAll(".list-group-item__programme__idea")
try {
    for (i=0; i<list__group__item__programme__idea.length; i++){
        list__group__item__programme__idea[i].addEventListener("mousemove", function(){
            ideaId = this.id
            for (i=0; i<card__programme__categorie.length; i++){
                    if (card__programme__categorie[i].id == ideaId && card__programme__categorie[i].textContent != "None"){
                        card__programme__categorie[i].style.display="flex"
                    }
            }
        })
        list__group__item__programme__idea[i].addEventListener("mouseleave", function(){
            for (i=0; i<card__programme__categorie.length; i++){
                card__programme__categorie[i].style.display="none"
            }
        })
    }
}
catch(e){
    console.error("C'est réussi");
}

//fonction qui fait disparaitre les seconde__ideas des third__ideas du programme si il sont == à "None"
let card__programme__categorie= document.querySelectorAll(".card__programme__categorie")
try {
    for(i=0; i<card__programme__categorie.length; i++){
        if (card__programme__categorie[i].textContent == "None"){
            card__programme__categorie[i].style.display="none"
        }
    }
}
catch{
    console.error("C'est réussi");
}


//autre fonction à commenter


try {
    if (window.location.href.indexOf("delete_sous_idee") > -1){
        if (main_categorie==null){
            for (i=0; i<card.length; i++){
                card[i].style.display="none"
            }
        }
    }
}
catch {
    console.error("C'est réussi");
}

try {
    for (i=0; i<sous_categorie.length; i++){
        if (sous_categorie[i].textContent != main_categorie.textContent){
            card[i].style.display="none"
        }
    }
}
catch {
    console.error("C'est réussi");
}

try {
    for (i=0; i<idea.length; i++){
        if (idea[i].textContent != categorie[i].textContent){
            list_sous[i].style.display="none"
        }
    }
}
catch {
    console.error("C'est réussi");
}

try {
    for (i=0; i<idea.length; i++){
        if (idea[i].textContent != rien[i].textContent){
            rienMain[i].style.display="none"
        }
    }
}
catch {
    console.error("C'est réussi");
}




