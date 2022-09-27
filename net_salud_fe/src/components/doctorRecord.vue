<script></script>

<template>
  <div id="rp" class="registro-medico">
    <form class="column">
      <input
        type="number"
        id="id"
        name="tipo"
        placeholder="Numero de identificación"
      />

      <input
        type="date"
        id="name"
        name="user_name"
        placeholder="Fecha de nacimiento"
      />

      <input
        type="text"
        id="name"
        name="user_name"
        placeholder="Nombres medico"
      />
      <input
        type="text"
        id="lastName"
        name="user_lastname"
        placeholder="Apellidos medico"
      />
      
      <input
        type="text"
        id="name"
        name="user_name"
        placeholder="Especialidad medico"
      />


      <input type="tel" id="name" name="user_name" placeholder="Celular" />
      <input type="text" id="name" name="user_name" placeholder="Dirección" />
      <input type="text" id="name" name="user_name" placeholder="Genero" />
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

.registro-medico {
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
