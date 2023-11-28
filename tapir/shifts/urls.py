from django.urls import path

from tapir.shifts import views

app_name = "shifts"
urlpatterns = [
    path("shift/<int:pk>/", views.ShiftDetailView.as_view(), name="shift_detail"),
    path(
        "shift/<int:pk>/printable",
        views.ShiftDetailView.as_view(
            template_name="shifts/shift_detail_printable.html"
        ),
        name="shift_detail_printable",
    ),
    path(
        "shift/<str:day>/day_printable",
        views.ShiftDayPrintableView.as_view(),
        name="shift_day_printable",
    ),
    path(
        "shift/<int:pk>/edit",
        views.EditShiftView.as_view(),
        name="shift_edit",
    ),
    path(
        "shift_template/<int:pk>/edit",
        views.EditShiftTemplateView.as_view(),
        name="shift_template_edit",
    ),
    path(
        "shift_template/create",
        views.ShiftTemplateCreateView.as_view(),
        name="shift_template_create",
    ),
    path(
        "shift_attendance/<int:pk>/<int:state>",
        views.UpdateShiftAttendanceStateView.as_view(),
        name="update_shift_attendance_state",
    ),
    path(
        "shift_attendance_form/<int:pk>/<int:state>",
        views.UpdateShiftAttendanceStateWithFormView.as_view(),
        name="update_shift_attendance_state_with_form",
    ),
    path(
        "shifttemplate/<int:pk>",
        views.ShiftTemplateDetail.as_view(),
        name="shift_template_detail",
    ),
    path(
        "shifttemplate/overview",
        views.ShiftTemplateOverview.as_view(),
        name="shift_template_overview",
    ),
    path(
        "slottemplate/<int:slot_template_pk>/register",
        views.RegisterUserToShiftSlotTemplateView.as_view(),
        name="slottemplate_register",
    ),
    path(
        "shiftslot/<int:slot_pk>/register/",
        views.RegisterUserToShiftSlotView.as_view(),
        name="slot_register",
    ),
    path(
        "shift_attendance_template/<int:pk>/delete",
        views.shift_attendance_template_delete,
        name="shift_attendance_template_delete",
    ),
    path(
        "calendar",
        views.ShiftCalendarView.as_view(),
        name="calendar",
    ),
    path(
        "shift_user_data/<int:pk>",
        views.EditShiftUserDataView.as_view(),
        name="edit_shift_user_data",
    ),
    path(
        "group_calendar",
        views.ShiftTemplateGroupCalendar.as_view(),
        name="shift_template_group_calendar",
    ),
    path(
        "group_calendar/<int:year>",
        views.ShiftTemplateGroupCalendar.as_view(),
        name="shift_template_group_calendar",
    ),
    path(
        "group_calendar/<int:year>/pdf",
        views.ShiftTemplateGroupCalendarAsPdf.as_view(),
        name="calendarpdf",
    ),
    path(
        "shift_account_entry/log/<int:user_pk>",
        views.UserShiftAccountLog.as_view(),
        name="user_shift_account_log",
    ),
    path(
        "shift_account_entry/create/<int:user_pk>",
        views.CreateShiftAccountEntryView.as_view(),
        name="create_shift_account_entry",
    ),
    path(
        "shift_exemption/create/<int:shift_user_data_pk>",
        views.CreateShiftExemptionView.as_view(),
        name="create_shift_exemption",
    ),
    path(
        "shift_exemption/<int:pk>/edit",
        views.EditShiftExemptionView.as_view(),
        name="edit_shift_exemption",
    ),
    path(
        "shift_exemption",
        views.ShiftExemptionListView.as_view(),
        name="shift_exemption_list",
    ),
    path(
        "statistics",
        views.StatisticsView.as_view(),
        name="statistics",
    ),
    path(
        "members_on_alert",
        views.MembersOnAlertView.as_view(),
        name="members_on_alert",
    ),
    path(
        "shift/<int:pk>/cancel",
        views.CancelShiftView.as_view(),
        name="cancel_shift",
    ),
    path(
        "shift/create",
        views.ShiftCreateView.as_view(),
        name="create_shift",
    ),
    path(
        "shift/<int:shift_pk>/slot/create",
        views.ShiftSlotCreateView.as_view(),
        name="create_slot",
    ),
    path(
        "shift_template/<int:shift_pk>/slot_template/create",
        views.ShiftSlotTemplateCreateView.as_view(),
        name="create_slot_template",
    ),
    path(
        "slot/<int:pk>/edit",
        views.ShiftSlotEditView.as_view(),
        name="edit_slot",
    ),
    path(
        "slot_template/<int:pk>/edit",
        views.ShiftSlotTemplateEditView.as_view(),
        name="edit_slot_template",
    ),
    path(
        "management",
        views.ShiftManagementView.as_view(),
        name="shift_management",
    ),
    path(
        "run_freeze_checks_manually",
        views.RunFreezeChecksManuallyView.as_view(),
        name="run_freeze_checks_manually",
    ),
    path(
        "generate_shifts_manually",
        views.GenerateShiftsManuallyView.as_view(),
        name="generate_shifts_manually",
    ),
    path(
        "statistics/slot_data_csv",
        views.slot_data_csv_view,
        name="slot_data_csv",
    ),
    path(
        "statistics/shift_template_data_csv_export",
        views.shift_template_data_csv_export,
        name="shift_template_data_csv_export",
    ),
    path(
        "statistics/shift_slot_template_data_csv_export",
        views.shift_slot_template_data_csv_export,
        name="shift_slot_template_data_csv_export",
    ),
    path(
        "statistics/shift_data_csv_export",
        views.shift_data_csv_export,
        name="shift_data_csv_export",
    ),
    path(
        "statistics/shift_slot_data_csv_export",
        views.shift_slot_data_csv_export,
        name="shift_slot_data_csv_export",
    ),
    path(
        "statistics/attendance_template_data_csv_export",
        views.attendance_template_data_csv_export,
        name="attendance_template_data_csv_export",
    ),
    path(
        "statistics/attendance_data_csv_export",
        views.attendance_data_csv_export,
        name="attendance_data_csv_export",
    ),
    path(
        "statistics/attendance_update_data_csv_export",
        views.attendance_update_data_csv_export,
        name="attendance_update_data_csv_export",
    ),
    path(
        "statistics/attendance_takeover_data_csv_export",
        views.attendance_takeover_data_csv_export,
        name="attendance_takeover_data_csv_export",
    ),
    path(
        "convert_shift_exemption_to_membership_pause/<int:pk>",
        views.ConvertShiftExemptionToMembershipPauseView.as_view(),
        name="convert_shift_exemption_to_membership_pause",
    ),
    path(
        "solidarity_shift_used/<int:pk>",
        views.SolidarityShiftUsed.as_view(),
        name="solidarity_shift_used",
    ),
    path(
        "solidarity_shift_given/<int:pk>",
        views.SolidarityShiftGiven.as_view(),
        name="solidarity_shift_given",
    ),
    path(
        "solidarity_shifts",
        views.SolidarityShiftsView.as_view(),
        name="solidarity_shifts",
    ),
    path(
        "solidarity_shifts/gifted_solidarity_shifts_json",
        views.GiftedSolidarityShiftsJsonView.as_view(),
        name="gifted_solidarity_shifts_json",
    ),
    path(
        "solidarity_shifts/used_solidarity_shifts_json",
        views.UsedSolidarityShiftsJsonView.as_view(),
        name="used_solidarity_shifts_json",
    ),
]
