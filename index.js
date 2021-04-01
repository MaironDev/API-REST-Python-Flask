const list = document.getElementById("list")

fetch('http://127.0.0.1:4000/products')
  .then(response => response.json())
  .then(data => return data );
  
  
  data.map(datos => ( 
    console.log (datos)
    
  ))

 console.log("Hola mundo")