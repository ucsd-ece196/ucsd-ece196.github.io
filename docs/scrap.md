

### Buttons

Now to see some Bootstrap in action, we first can style our checkboxes. Remove the "Select All" button and replace the entire `<form>` with this:

    <form v-on:change="updateColor()">
        <div class="btn-group btn-group-toggle" data-toggle="buttons">
            <label class="btn btn-secondary" v-bind:class="{active: color.r}">
                <input type="checkbox" v-model="color.r" > Red
            </label>
            <label class="btn btn-secondary" v-bind:class="{active: color.g}">
                <input type="checkbox" v-model="color.g"> Green
            </label>
            <label class="btn btn-secondary" v-bind:class="{active: color.b}">
                <input type="checkbox" v-model="color.b"> Blue
            </label>
            <button v-if="color.r && color.g && color.b" class="btn btn-secondary" type="button" v-on:click="selectAll(false); updateColor()">Deselect All</button>
            <button v-else class="btn btn-secondary" type="button" v-on:click="selectAll(true); updateColor()">Select All</button>
        </div>
    </form>

Refresh the page and we see a few new things are going on here:

1. The buttons are wrapped in a new div of `class="btn-group btn-group-toggle"`. This is actually two classes:
    * `btn-group` turns the buttons into a single bar
    * `btn-group-toggle` replaces checkboxes with toggle buttons
2. Each label gained 3 new classes:
    * `btn` makes it a button shape
    * `btn-secondary` makes it the secondary color
    * `v-bind:class="{active: color.r}"` adds the `active` class depending on whether the value is `true`. This will make the button look darker when it is checked.
3. We also added a Deselect All button. Not entirely related, but allows us to see the transitions better.