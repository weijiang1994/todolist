<template>
  <div id="app">
    <h1>待办事项</h1>
    <TodoList/>
  </div>
</template>

<script>
import TodoList from './components/TodoList.vue'
export default {
  components:{
    TodoList
  }
}
</script>

<style>

  *, *::before, *::after{
    box-sizing: border-box;
  }
  #app{
    max-width: 600px;
    margin: 0 auto;
    line-height: 1.4;
    font-family: 'Microsoft YaHei', Arial, Helvetica, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #32485F;
    border: 1px solid rgb(215, 216, 215);
    padding: 15px;
    border-radius: 5px;
    box-shadow: 10px 10px 4px rgb(123, 197, 240);
  }
  h1 {
	text-align: center;
}
</style>