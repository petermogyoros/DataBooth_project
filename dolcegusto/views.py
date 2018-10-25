from django.shortcuts import render
from django.views import View

from dolcegusto.models import past_week_scrap

class Line(View):
    model = past_week_scrap

    def get(self, request):

        try:
            day_1_side_a_ng = int(past_week_scrap(self)[0])
            day_1_side_b_ng = int(past_week_scrap(self)[1])
            day_1_side_a_re = int(past_week_scrap(self)[2])
            day_1_side_b_re = int(past_week_scrap(self)[3])

        except:
            day_1_side_a_ng = 0
            day_1_side_b_ng = 0
            day_1_side_a_re = 0
            day_1_side_b_re = 0


        try:
            day_2_side_a_ng = int(past_week_scrap(self)[4])
            day_2_side_b_ng = int(past_week_scrap(self)[5])
            day_2_side_a_re = int(past_week_scrap(self)[6])
            day_2_side_b_re = int(past_week_scrap(self)[7])

        except:
            day_2_side_a_ng = 0
            day_2_side_b_ng = 0
            day_2_side_a_re = 0
            day_2_side_b_re = 0


        try:
            day_3_side_a_ng = int(past_week_scrap(self)[8])
            day_3_side_b_ng = int(past_week_scrap(self)[9])
            day_3_side_a_re = int(past_week_scrap(self)[10])
            day_3_side_b_re = int(past_week_scrap(self)[11])

        except:
            day_3_side_a_ng = 0
            day_3_side_b_ng = 0
            day_3_side_a_re = 0
            day_3_side_b_re = 0


        try:
            day_4_side_a_ng = int(past_week_scrap(self)[12])
            day_4_side_b_ng = int(past_week_scrap(self)[13])
            day_4_side_a_re = int(past_week_scrap(self)[14])
            day_4_side_b_re = int(past_week_scrap(self)[15])

        except:
            day_4_side_a_ng = 0
            day_4_side_b_ng = 0
            day_4_side_a_re = 0
            day_4_side_b_re = 0


        try:
            day_5_side_a_ng = int(past_week_scrap(self)[16])
            day_5_side_b_ng = int(past_week_scrap(self)[17])
            day_5_side_a_re = int(past_week_scrap(self)[18])
            day_5_side_b_re = int(past_week_scrap(self)[19])

        except:
            day_5_side_a_ng = 0
            day_5_side_b_ng = 0
            day_5_side_a_re = 0
            day_5_side_b_re = 0


        try:
            day_6_side_a_ng = int(past_week_scrap(self)[20])
            day_6_side_b_ng = int(past_week_scrap(self)[21])
            day_6_side_a_re = int(past_week_scrap(self)[22])
            day_6_side_b_re = int(past_week_scrap(self)[23])

        except:
            day_6_side_a_ng = 0
            day_6_side_b_ng = 0
            day_6_side_a_re = 0
            day_6_side_b_re = 0


        try:
            day_7_side_a_ng = int(past_week_scrap(self)[24])
            day_7_side_b_ng = int(past_week_scrap(self)[25])
            day_7_side_a_re = int(past_week_scrap(self)[26])
            day_7_side_b_re = int(past_week_scrap(self)[27])

        except:
            day_7_side_a_ng = 0
            day_7_side_b_ng = 0
            day_7_side_a_re = 0
            day_7_side_b_re = 0


        return render(request, "dolcegusto/line.html", {
        "day_1_side_a_ng": day_1_side_a_ng, "day_1_side_b_ng": day_1_side_b_ng,
        "day_1_side_a_re": day_1_side_a_re, "day_1_side_b_re": day_1_side_b_re,
        "day_2_side_a_ng": day_2_side_a_ng, "day_2_side_b_ng": day_2_side_b_ng,
        "day_2_side_a_re": day_2_side_a_re, "day_2_side_b_re": day_2_side_b_re,
        "day_3_side_a_ng": day_3_side_a_ng, "day_3_side_b_ng": day_3_side_b_ng,
        "day_3_side_a_re": day_3_side_a_re, "day_3_side_b_re": day_3_side_b_re,
        "day_4_side_a_ng": day_4_side_a_ng, "day_4_side_b_ng": day_4_side_b_ng,
        "day_4_side_a_re": day_4_side_a_re, "day_4_side_b_re": day_4_side_b_re,
        "day_5_side_a_ng": day_5_side_a_ng, "day_5_side_b_ng": day_5_side_b_ng,
        "day_5_side_a_re": day_5_side_a_re, "day_5_side_b_re": day_5_side_b_re,
        "day_6_side_a_ng": day_6_side_a_ng, "day_6_side_b_ng": day_6_side_b_ng,
        "day_6_side_a_re": day_6_side_a_re, "day_6_side_b_re": day_6_side_b_re,
        "day_7_side_a_ng": day_7_side_a_ng, "day_7_side_b_ng": day_7_side_b_ng,
        "day_7_side_a_re": day_7_side_a_re, "day_7_side_b_re": day_7_side_b_re,
        })

# Create your views here.
# class Line8(View):
#     model = DolceGusto_table
#
#     def get(self, request):
#         value_dict = {}
#
#         # loop counters
#         counter_raw_time = 0
#         counter_a_ok = 0
#         counter_b_ok = 0
#         counter_line = 0
#
#         raw_time_sum = 0
#         a_ok_sum = 0
#         b_ok_sum = 0
#         line_sum = 0
#
#         for q in qs:
#             q = str(q)
#             q_individual_values = q.split()
#             object_counter = 0
#             for k in q_individual_values:
#                 object_counter += 1
#                 if object_counter == 1:
#                     value_dict.setdefault("raw_time", [])
#                     value_dict["raw_time"].append(int(k))
#                 elif object_counter == 2:
#                     value_dict.setdefault("line", [])
#                     value_dict["line"].append(int(k))
#                 elif object_counter == 3:
#                     value_dict.setdefault("batch", [])
#                     value_dict["batch"].append(int(k))
#                 elif object_counter == 4:
#                     value_dict.setdefault("a_ok", [])
#                     value_dict["a_ok"].append(int(k))
#                 elif object_counter == 5:
#                     value_dict.setdefault("b_ok", [])
#                     value_dict["b_ok"].append(int(k))
#                 elif object_counter == 6:
#                     value_dict.setdefault("combined_side_a_ng", [])
#                     value_dict["combined_side_a_ng"].append(int(k))
#                 elif object_counter == 7:
#                     value_dict.setdefault("combined_side_b_ng", [])
#                     value_dict["combined_side_b_ng"].append(int(k))
#         print(value_dict)
#         # this is probably going to be a function
#         for raw_time in value_dict["raw_time"]:
#             counter_raw_time += 1
#             raw_time_sum = raw_time_sum + raw_time
#         for a_ok in value_dict["a_ok"]:
#             counter_a_ok += 1
#             a_ok_sum = a_ok_sum + a_ok
#         for b_ok in value_dict["b_ok"]:
#             counter_b_ok += 1
#             b_ok_sum = b_ok_sum + b_ok
#         for line in value_dict["line"]:
#             counter_line += 1
#             line_sum = line_sum + line
#
#         a_ok_avarage = a_ok_sum/counter_a_ok
#         b_ok_avarage = b_ok_sum/counter_b_ok
#         raw_time_avarage = raw_time_sum/counter_raw_time
#         line_avarage = line_sum/counter_line
#
#         return render(request, "dolcegusto/line.html",
#         {"raw_time": int(raw_time_avarage), "line": int(line_avarage),
#         "a_ok": int(a_ok_avarage), "b_ok": int(b_ok_avarage)})
