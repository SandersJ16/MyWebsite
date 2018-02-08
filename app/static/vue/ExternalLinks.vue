<template>
    <external-link v-bind:class="visibility" icon="github" url="https://github.com/SandersJ16/"></external-link>
    <external-link v-bind:class="visibility" icon="linkedin" url="https://www.linkedin.com/in/justinsanderscodemastersupreme/"></external-link>
</template>

<script>
    import ExternalLink from './ExternalLink.vue'

    export default {
      name: "external-links",
      props: ['visibility'],

      components: {
            ExternalLink,
        },
    }
</script>
