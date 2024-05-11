
document.addEventListener('DOMContentLoaded', function() {
  // 获取借阅状态下拉菜单和借阅人下拉菜单
  var statusSelect = document.getElementById('status');
  var borrowerSelect = document.getElementById('borrower');

  // 监听借阅状态下拉菜单的变化
  statusSelect.addEventListener('change', function() {
    // 获取所选借阅状态的值
    var selectedStatus = statusSelect.value;

    // 如果借阅状态为“已借出”
    if (selectedStatus === "B") {
      // 将借阅人下拉菜单禁用，并将其值清空
      borrowerSelect.disabled = true;
      borrowerSelect.value = "";
    } else {
      // 否则启用借阅人下拉菜单
      borrowerSelect.disabled = false;
    }
  });

  // 监听借阅人下拉菜单的变化
  borrowerSelect.addEventListener('change', function() {
    // 如果选择了借阅人，则将借阅状态设为“已借出”
    statusSelect.value = "B";
  });

  // 初始化时检查借阅状态
  checkBorrowerAvailability();

  // 监听借阅状态下拉菜单的变化
  statusSelect.addEventListener('change', checkBorrowerAvailability);

  // 检查借阅人下拉菜单的可用性
  function checkBorrowerAvailability() {
    var selectedStatus = statusSelect.value;

    // 如果借阅状态为“可以借阅”或“不可借阅”，则禁用借阅人下拉菜单
    if (selectedStatus === "Y" || selectedStatus === "N") {
      borrowerSelect.disabled = true;
      borrowerSelect.value = "";
    } else {
      borrowerSelect.disabled = false;
    }
  }
});
