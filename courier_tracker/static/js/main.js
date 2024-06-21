document.addEventListener('DOMContentLoaded', (event) => {
    const shipmentStatusEditables = document.querySelectorAll('.shipment_status');

    // check if the editable element is equivalent to a certain shipment status
    // if delivered = (class = success), picked_up = (class = danger),
    // In transit = (class = warning)
    const legalCharsToCheck = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    let shipment_status = ''
    let totalCharsInShipmentStatus = 0

    shipmentStatusEditables.forEach((element) => {
        element.addEventListener('keydown', (event) => {

        // check if we are pressing spacebar then we shud add a space to the shipment status word
        if(event.keyCode === 32){
            shipment_status += ' '
        }

        // check if we are pressing backspace, then remove the last character
        // from the shipment status and update the total remaining characters
        if(event.keyCode === 8 && totalCharsInShipmentStatus !== -1){
            shipment_status = shipment_status.slice(0, -1)
            totalCharsInShipmentStatus -= 1
        }

        // check if we are pressing a legal character, then add it to the shipment status as a word
        // and update the total number of remaining characters
        if(legalCharsToCheck.includes(event.key)){
            shipment_status += event.key
            totalCharsInShipmentStatus += 1

            if(shipment_status === 'delivered'){
                shipment_status = 'delivered'
                element.classList = 'bg-success text-white'
            }

            else if(shipment_status === 'in transit'){
                shipment_status = 'in transit'
                element.classList = 'bg-warning text-white'
            }

            else if(shipment_status === 'picked up'){
                shipment_status = 'picked up'
                element.classList = 'bg-danger text-white'
            }

            else{
                element.classList = 'bg-secondary text-white'
            }

        }
    });
    })



});