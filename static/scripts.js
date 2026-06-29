document.addEventListener('DOMContentLoaded', function() {
  const rows = document.querySelectorAll('table tbody tr');
  rows.forEach(row => {
    row.addEventListener('mouseenter', () => {
      row.classList.add('shadow-sm');
    });
    row.addEventListener('mouseleave', () => {
      row.classList.remove('shadow-sm');
    });
  });
});
