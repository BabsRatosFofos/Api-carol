async function buscarUsuarios() {
    const resposta = await fetch("/usuarios");
  
    const usuarios = await resposta.json();
  
    const corpo = document.getElementById("corpoTabela");
    corpo.innerHTML = "";
  
    usuarios.forEach(usuario => {
      const tr = document.createElement("tr");
      tr.innerHTML = `
        <td>${usuario.name}</td>
        <td>${usuario.email}</td>
        <td>${usuario.phone}</td>
      `;
      corpo.appendChild(tr);
    });
  }