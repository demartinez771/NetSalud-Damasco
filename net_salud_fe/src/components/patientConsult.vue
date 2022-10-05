<script></script>

<template>
  <div id="rp" class="consultar-paciente">
    <form class="row">      
      <input
        type="text"
        id="username"
        name="tipo"
        placeholder="digite la cédula"
      />
    
      <button v-on:click="loadRecord">Consultar</button>
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

.consultar-paciente {
  margin-top: 50px;
  padding: 0%;
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

form {
  width: 400px;
  height: 600px;
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