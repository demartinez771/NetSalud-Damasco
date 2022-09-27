<script></script>

<template>
  <div id="rp" class="registro-familiar">
    <form class="column">
      <input
        type="number"
        id="id"
        name="tipo"
        placeholder="Documento de identificacion"
      />

      
      <input
        type="text"
        id="name"
        name="user_name"
        placeholder="Parentesco"
      />
      
      <input type="email" id="name" name="user_name" placeholder="Correo electronico" />
      

      <input
        type="text"
        id="name"
        name="user_name"
        placeholder="Username del Paciente"
      />

      <input
        type="number"
        id="name"
        name="user_name"
        placeholder="Documento del paciente"
      />
     
      <button v-on:click="loadRecord">Registrar</button>
    </form>
  </div>
</template>

<style>
.row {
  display: flex;
  flex-direction: row;
}
.column {
  display: flex;
  flex-direction: column;
}

.registro-familiar {
  margin-top: 50px;
  padding: 0%;
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

form {
  width: 747px;
  height: 648px;
  display: flex;
  background: #e3f2fd;
  border-radius: 20px;
  justify-content: space-evenly;
  align-items: center;
  border: 5px solid #2e2d4d;
}

input {
  width: 400px;
  height: 40px;
  background: #fafafa;
  font-family: "Kanit";
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 45px;
  text-align: center;
  border-radius: 10px;
  color: #8aa29e;
}
button {
  width: 300px;
  height: 50px;
  background: #2e2d4d;
  border-radius: 10px;
  font-family: "Kanit";
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 45px;
  text-align: center;

  color: #fafafa;
}
</style>