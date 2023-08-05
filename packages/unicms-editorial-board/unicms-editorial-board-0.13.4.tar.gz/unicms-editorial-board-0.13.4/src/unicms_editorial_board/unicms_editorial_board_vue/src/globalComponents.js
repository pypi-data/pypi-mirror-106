//import BaseInput from './components/Inputs/BaseInput.vue'
//import BaseCheckbox from './components/Inputs/BaseCheckbox.vue'
//import BaseRadio from './components/Inputs/BaseRadio.vue'
import BaseDropdown from './components/BaseDropdown.vue'
//import Card from './components/Cards/Card.vue'
import Alerts from './components/Alerts/Alerts.vue'
import DjangoForm from './components/Forms/DjangoForm.vue'

/**
 * You can register global components here and use them as a plugin in your main Vue instance
 */

const GlobalComponents = {
  install (Vue) {
    //Vue.component(BaseInput.name, BaseInput)
    //Vue.component(BaseCheckbox.name, BaseCheckbox)
    //Vue.component(BaseRadio.name, BaseRadio)
    Vue.component(BaseDropdown.name, BaseDropdown)
    Vue.component(DjangoForm.name, DjangoForm)
    Vue.component(Alerts.name, Alerts)
    //Vue.component('card', Card)
  }
}

export default GlobalComponents
