let ValorPacote = 0;
let ValorAdicionais = 0;
let coisas =0;

function CalcularTotalViagem()
{
    ValorAdicionais = 0;
    coisas = 0
    CalcularPacotes()
    CalcularAdicionais()
   document.getElementById("caixona").innerHTML = `${ValorAdicionais}`;
   document.getElementById("coisas").innerHTML = `${coisas}`;
   


}
function CalcularAdicionais(){

    let tamanho = document.querySelectorAll("input[name='adicionais']").length
    let adicionais = document.querySelectorAll("input[name='adicionais']")
    for (var i = 0; i< tamanho ; i++)
    {
        if(adicionais[i].checked == true){
            ValorAdicionais += Number(adicionais[i].value);
            console.log(adicionais[i].id)
           coisas += ` /${adicionais[i].id}`
        }
    }
   
}
function CalcularPacotes(){

    let tamanho = document.querySelectorAll("input[name='Pacote']").length
    let Pacotes = document.querySelectorAll("input[name='Pacote']")
    for (var i = 0; i< tamanho ; i++)
    {
        if(Pacotes[i].checked == true){
            console.log(Pacotes[i].id)
            console.log(Pacotes[i].value)
            ValorAdicionais += Number(Pacotes[i].value);
            break;
        }
    }
}

