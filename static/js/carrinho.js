const main = document.querySelector('#main')
const preco_total = document.querySelector('#preco-total')
let valor_total = []

let getValor = (objects) => {
    let valorzao = 0
    for (const object of objects){
        valorzao += object.valor
    }
    return valorzao
}

for (const children of main.children){
    children.children[1].children[4].innerHTML += children.children[1].children[3].innerHTML.substring(18)
    let valor = Number(children.children[1].children[3].innerHTML.substring(18))
    valor_total.push({id: children.id, valor: valor})
    preco_total.innerHTML = `R$ ${getValor(valor_total)}`
    children.children[1].children[2].children[0].addEventListener('change', () => {
        const valor = Number(children.children[1].children[3].innerHTML.substring(18)) * Number(children.children[1].children[2].children[0].value)
        children.children[1].children[4].innerHTML = `Preço total: R$ ${valor.toFixed(2)}`
        let index = valor_total.indexOf(valor_total.find((object) => object.id === children.id))
        valor_total[index] = {id: children.id, valor: valor}
        preco_total.innerHTML = `R$ ${getValor(valor_total)}`
    })

}

