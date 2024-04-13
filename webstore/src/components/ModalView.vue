
  <template>
    <div class="modal-backdrop">
      <div class="modal">
        <header class="modal-header">
          <slot name="header">
            <button
              type="button"
              class="btn-close"
              @click="close"
            >
              x
            </button>
          </slot>
        </header>
        <section class="modal-body">
          <img src="../assets/home.png" />
        </section>
        <footer class="modal-footer"></footer>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "ModalItem",
    data() {
      return {};
    },
    methods: {
      close() {
        this.$emit("closeItem");
      },
    },
    components: {},
  };
  </script>
  
  <style>
  .modal-backdrop {
    z-index: 9999;
    margin-top: 18px;
    margin-left: auto;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .modal {
    max-height: 349px;
    max-width: 349px;
    border-radius: 35px;
    background: #8d8c8c;
    overflow-x: auto;
    display: flex;
    margin-right: 100px;
    flex-direction: column;
  }
  
  .modal-header {
    display: flex;
    align-content: center;
    color: #8d8c8c;
    justify-content: flex-end;
  }
  
  .modal-footer {
    justify-content: flex-end;
  }
  
  .modal-body {
    display: flex;
    flex-direction: column;
    position: relative;
    padding: 10px 10px;
  }
  
  .btn-close {
    border: none;
    font-size: 36px;
    padding-right: 15px;
    cursor: pointer;
    font-weight: 1000;
    font-family: "Sofia Sans";
    color: #424242;
    background: #ffffff;
  }
  
  a:link {
    text-decoration: none;
    color: black;
  }
  
  a:visited {
    text-decoration: none;
    color: black;
  }
  </style>
  