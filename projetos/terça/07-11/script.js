let ValorAdicionais;
let coisas;
let ValorLanche
let ValorTotal
let ValorFrete
function CalcularTotal()
{

    ValorLanche = Number(document.getElementById("Combo").value);
    add();
    frete()
    ValorTotal = ValorAdicionais + ValorLanche  + ValorFrete
    document.getElementById("TotalPagar").value =`R$ ${ValorTotal},00`
    document.getElementById("floatingTextarea2").innerHTML =`O combo custara R$${ValorLanche},00 , os adicionais R$${ValorAdicionais},00 e o frete ${ValorFrete}`

}

function add(){
    ValorAdicionais = 0;
    let tamanho = document.querySelectorAll("input[name='adicionais']").length;
    let adicionais = document.querySelectorAll("input[name='adicionais']:checked");
    for (var i = 0; i< tamanho ; i++)
    {
        if(adicionais[i]){
            ValorAdicionais += Number(adicionais[i].value);
            console.log(ValorAdicionais)
        }
    }
}

function frete(){
    ValorFrete = 0;
    let entregas = document.querySelectorAll("input[name='flexRadioDefault']")
    for (let i = 0; i< entregas.length ; i++)
        if(entregas[i].checked){
            ValorFrete = Number(entregas[i].value);
            break;
        }
    }


