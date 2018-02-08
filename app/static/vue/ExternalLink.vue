<template>
    <a class="navbar-item" v-bind:href="url" target="_blank">
        <span class="icon has-text-primary neutral">
            <i class="fa fa-2x" v-bind:class="fa-icon"></i>
        </span>
        <span class="icon has-text-white hovered">
            <i class="fa fa-2x" v-bind:class="fa-icon"></i>
        </span>
    </a>
</template>

<script>
    export default {
      name: "external-link",
      props: ['icon', 'url'],

      computed: {
        fa-icon: function() {
            return "fa-" + this.icon
        }
      }
    }
</script>
