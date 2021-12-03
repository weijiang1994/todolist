<template>
  <div class="todolist">
    <BaseInput
      v-model="newTodoText"
      placeholder="输入新的待办事项!"
      @keydown.enter="addTodo"
    />
    <ul v-if="todos.length">
      <TodoListItem
        v-for="todo in todos"
        :key="todo.id"
        :todo="todo"
        @remove="removeTodo"
      />
    </ul>
    <p v-else><b>你还没有最近待办事项~</b></p>
    <div v-if="todos.length" class="hint">
      <p>TodoList只会保存一天哦，每天凌晨2点后端服务会自动重启！</p>
    </div>
  </div>
</template>

<script>
// 导入需要使用到的子组件
import BaseInput from "./BaseInput.vue";
import TodoListItem from "./TodoListItem.vue";

// 设置组件的相关属性,并将其暴露给其他模块
export default {
  components: {
    BaseInput,
    TodoListItem,
  },
  data() {
    return {
      newTodoText: "",
      todos: [],
    };
  },
  methods: {
    // 添加TodoList
    addTodo() {
      const trimmedText = this.newTodoText.trim();
      if (trimmedText) {
        fetch(`${process.env.VUE_APP_BACKEND_URL}/add-todolist`, {
          mode: "cors",
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ text: trimmedText }),
        })
          .then((res) => res.json())
          .then((data) => {
            if (data.code === 200) {
              this.todos.push({
                id: data.id,
                text: trimmedText,
              });
              this.newTodoText = "";
            }
          });
      }
    },

    // 移除TodoList
    removeTodo(idToRemove) {
      // 自定义信号'remove'的响应函数, idToRemove为发射信号时候携带的参数(有点类似QT的信号槽机制)
      fetch(`${process.env.VUE_APP_BACKEND_URL}/remove-todolist`, {
        method: "POST",
        mode: "cors",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ id: idToRemove }),
      })
        .then((res) => res.json())
        .then((data) => {
          if (data.code === 200) {
            this.todos = this.todos.filter((todo) => {
              return todo.id !== idToRemove;
            });
          } else {
            alert(data.msg);
          }
        });
    },

    // 获取服务端的TodoList
    getTodoList() {
      fetch(`${process.env.VUE_APP_BACKEND_URL}/get-todolist`, {
        method: "GET",
        mode: "cors",
      })
        .then((res) => res.json())
        .then((data) => {
          this.todos = data;
        });
    },
  },

  mounted() {
    // 组件挂载后立即执行获取数据的方法,可以去了解一下Vue的生命周期、组件的生命周期相关内容
    return this.getTodoList();
  },
};
</script>

<style scoped>
ul {
  list-style: none;
  padding: 5px;
  max-height: 500px;
  overflow-y: auto;
}
.hint {
  font-size: 12px;
  font-weight: bold;
  text-align: center;
}
</style>