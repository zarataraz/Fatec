function CaucularDesconto(){
   let tamanho = document.querySelectorAll("input[name='Pacote']").length;
   console.log(tamanho)


   let pacotes = document.querySelectorAll("input[name='Pacote']");
    console.log(pacotes)

    for(var i = 0 ; i < tamanho; i++)
    {
        console.log(pacotes[i].value);
    }
}