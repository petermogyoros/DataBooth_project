from django.shortcuts import render
from django.views import View

from dolcegusto.models import Past_Week

class Line(View):
    model = Past_Week

    def get(self, request):
        pass

        # return render(request, "dolcegusto/line.html", {"side_a_ng": int(scrap_rate(self)[0]), "side_b_ng": int(scrap_rate(self)[1]),
        # "side_a_re": int(scrap_rate(self)[2]), "side_b_re": int(scrap_rate(self)[3])})

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
