const main = document.querySelector('#main')
const preco_total = document.querySelector('#preco-total')

for (const children of main.children){
    children.children[1].children[4].innerHTML += children.children[1].children[3].innerHTML.substring(18)
    preco_total.innerHTML = `R$ ${Number(preco_total.innerHTML.substring(3)) +  Number(children.children[1].children[3].innerHTML.substring(18))}` 
    children.children[1].children[2].children[0].addEventListener('change', () => {
        const valor = Number(children.children[1].children[3].innerHTML.substring(18)) * Number(children.children[1].children[2].children[0].value)
        children.children[1].children[4].innerHTML = `Preço total: R$ ${valor}`
        preco_total.innerHTML = `R$ ${Number(preco_total.innerHTML.substring(3)) +  valor}`
    })

}

