async function buscarUsuarios() {
    const resposta = await fetch("/usuarios");
  
    const usuarios = await resposta.json();
  
    const lista = document.getElementById("listaUsuarios");
    lista.innerHTML = "";

    usuarios.forEach(usuario => {
      const li = document.createElement("li");
      li.textContent = `${usuario.name} - ${usuario.email} - ${usuario.phone}`;
      lista.appendChild(li);
    });
  }