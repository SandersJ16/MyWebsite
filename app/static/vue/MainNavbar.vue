<template>
    <nav id="navbar" class="navbar is-black">
        <div class="navbar-brand">
            <a class="navbar-item" href="/">
                <img v-bind:src="Flask.url('static', {'filename': 'img/JustinSanders.svg'})" alt="Justin Sanders" class="header_logo">
            </a>
            <!-- Display only on mobile screen devies -->
             <external-links visibility="is-hidden-desktop"></external-links>
            <div class="navbar-burger" v-on:click="toggleMenu" v-bind:class="{ 'is-active': hamburger_active }">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>

        <div class="navbar-menu" v-bind:class="{ 'is-active': hamburger_active }">
            <div class="navbar-start">
                <a class="navbar-item" href="/about">
                    About Me
                </a>
                <a class="navbar-item" href="/resume">
                    Resume
                </a>
            </div>

            <div class="navbar-end is-hidden-touch">
                <span class="navbar-item">Welcome, {{ config.user.nickname || "Guest" }}</span>
                <!-- Display only on full screen devices -->
                <external-links visibility=""></external-links>
            </div>
        </div>
    </nav>
</template>


<script>
    import ExternalLinks from './ExternalLinks.vue'

    export default {
      name: 'main-navbar',

      components: {
            ExternalLinks,
      },

      data: function() {
        hamburger_active: false
      },
      // bind event handlers to the `handleResize` method
      mounted: function () {
        window.addEventListener('resize', this.untoggleHamburger);
      },
      beforeDestroy: function () {
        window.removeEventListener('resize', this.untoggleHamburger);
      },
      methods: {
        toggleMenu: function () {
          this.hamburger_active = !this.hamburger_active;
        },
        untoggleHamburger: function () {
            this.hamburger_active = false;
        }
      }
    }
</script>

<style lang='scss'>
    .navbar-menu.is-active {
        position: absolute;
        right: 0;
    }
    a.navbar-item:hover {
        .icon.neutral {
            display: none;
        }
        .icon.hovered {
            display: initial;
        }
    }
    a.navbar-item {
        .icon.neutral {
            display: initial;
        }
        .icon.hovered {
            display: none;
        }
    }
</style>
