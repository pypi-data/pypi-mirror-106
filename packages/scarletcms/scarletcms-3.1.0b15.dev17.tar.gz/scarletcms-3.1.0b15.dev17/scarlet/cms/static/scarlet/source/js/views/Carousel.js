import { View } from 'backbone'
import { clickOpenModal } from 'helpers/Modal'

const CarouselItem = View.extend({
    initialize () {
      this.$button = this.$('add_crousel_item')
    },

    events: {
        'click .add_carousel_item': 'handleModal',
    },

    handleModal (e) {
        e.preventDefault()
        clickOpenModal(e, 'add_crousel_item')
    }
})

export default CarouselItem
