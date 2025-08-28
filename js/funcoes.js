document.addEventListener('DOMContentLoaded', function () {
  // Live Alert
  var alertPlaceholder = document.getElementById('liveAlertPlaceholder');
  var alertTrigger = document.getElementById('liveAlertBtn');
  function showAlert(message, type) {
    var wrapper = document.createElement('div');
    wrapper.innerHTML = [
      `<div class="alert alert-${type} alert-dismissible" role="alert">`,
      `   ${message}`,
      '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
      '</div>'
    ].join('');
    alertPlaceholder.append(wrapper);
  }
  if (alertTrigger) {
    alertTrigger.addEventListener('click', function () {
      showAlert('Nice, you triggered this alert message!', 'success');
    });
  }

  // Popover
  var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
  var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
    return new bootstrap.Popover(popoverTriggerEl);
  });

  // Tooltip
  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
  var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
  });

  // Toast
  var toastElList = [].slice.call(document.querySelectorAll('.toast'));
  var toastList = toastElList.map(function (toastEl) {
    return new bootstrap.Toast(toastEl);
  });
  toastList.forEach(function (toast) { toast.show(); });

  // Scrollspy
  var scrollSpyEl = document.querySelector('[data-bs-spy="scroll"]');
  if (scrollSpyEl) {
    bootstrap.ScrollSpy.getOrCreateInstance(scrollSpyEl);
  }
});

