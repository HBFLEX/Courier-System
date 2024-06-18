document.addEventListener('DOMContentLoaded', (event) => {
    var shipmentItemModal = document.getElementById('shipmentItemModal');
    shipmentItemModal.addEventListener('show.bs.modal', function (event) {
        // Button that triggered the modal
        var button = event.relatedTarget;

        // Extract info from data-* attributes
        var shipmentId = button.getAttribute('data-id');
        var trackingId = button.getAttribute('data-tracking-id');

        // Update the modal's content
        var modalShipmentId = shipmentItemModal.querySelector('#modal-shipment-id');
        var modalTrackingId = shipmentItemModal.querySelector('#modal-tracking-id');

        modalShipmentId.textContent = shipmentId;
        modalTrackingId.textContent = trackingId;

        // Add more fields as needed
    });
});