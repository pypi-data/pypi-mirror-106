ls -al
import pandas as pd
from collections import Counter
df = pd.read_csv('onow_chatbot_timestamp_tangible.csv.gz')
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
le.fit(df['attribute'])
df['attribute_num'] = le.transform(df['attribute'])
df.describe(include='all')
le.classes_
countsan = Counter(df['attribute_num'])
countsa = Counter(df['attribute'])
countsa2 = {le.classes_[k]:v for (k,v) in countsan.items()}
countsa2
pd.DataFrame([countsa, countsa2])
import json
json.dump?


"""
>>> %run numericize_attributes.py
>>> who
>>> import pandas as pd
... from collections import Counter
... df = pd.read_csv('onow_chatbot_timestamp_tangible.csv.gz')
... from sklearn import preprocessing
... le = preprocessing.LabelEncoder()
... le.fit(df['attribute'])
... df['attribute_num'] = le.transform(df['attribute'])
... df.describe(include='all')
... le.classes_
... countsan = Counter(df['attribute_num'])
... countsa = Counter(df['attribute'])
... countsa2 = {le.classes_[k]:v for (k,v) in countsan.items()}
... countsa2
... pd.DataFrame([countsa, countsa2])
...
   coaching_3.3_goal_complete  coaching_3.3_appearance  ...  coaching_student_name  salesforce_business_id
0                       56662                    48304  ...                     36                      27
1                       56662                    48304  ...                     36                      27

[2 rows x 601 columns]
>>> ls.classes_
>>> le.classes_
array(['birth_year', 'biz_dead_covid', 'biz_dead_date_closed',
       'biz_dead_goals', 'biz_dead_reason', 'biz_health_status',
       'biz_industry', 'biz_name', 'biz_owner', 'biz_paused_covid_reason',
       'biz_paused_date_paused', 'biz_paused_notes', 'biz_paused_reason',
       'biz_paused_when_reopen', 'biz_pivot_covid', 'biz_pivot_date',
       'biz_pivot_new_industry', 'biz_pivot_new_name', 'biz_pivot_notes',
       'biz_pivot_reason', 'bizsur_mmod1_status', 'bizsur_mmod2_status',
       'bizsur_mmod3_status', 'bizsur_mmod4_status',
       'bizsur_mmod5_status', 'bizsur_mmod6_status', 'bizsur_mod1_status',
       'bizsur_mod2_status', 'bizsur_status', 'bmb_channels_complete',
       'bmb_channels_primary_acquisition',
       'bmb_channels_primary_delivery', 'bmb_channels_start',
       'bmb_cr_complete', 'bmb_cr_product_customers_count',
       'bmb_cr_products_per_customer', 'bmb_cr_return',
       'bmb_cr_service_customers_count', 'bmb_cr_services_per_customer',
       'bmb_cr_start', 'bmb_cr_style', 'bmb_customer_segments_age',
       'bmb_customer_segments_complete', 'bmb_customer_segments_gender',
       'bmb_customer_segments_location',
       'bmb_customer_segments_special_interest',
       'bmb_customer_segments_start', 'bmb_expense_complete',
       'bmb_expense_daily_food_cost', 'bmb_expense_employee_detail',
       'bmb_expense_have_maintainence_cost',
       'bmb_expense_having_employees', 'bmb_expense_inventory_inputs',
       'bmb_expense_inventory_inputs_detail',
       'bmb_expense_inventory_inputs_simple', 'bmb_expense_irregular',
       'bmb_expense_marketing_detail',
       'bmb_expense_monthly_employee_cost',
       'bmb_expense_monthly_general_cost',
       'bmb_expense_monthly_health_cost',
       'bmb_expense_monthly_maintainence_cost',
       'bmb_expense_monthly_marketing_cost',
       'bmb_expense_monthly_other_operation_cost',
       'bmb_expense_monthly_transport_cost',
       'bmb_expense_operation_cost_detail',
       'bmb_expense_operation_cost_simple',
       'bmb_expense_option_to_observe', 'bmb_expense_other_personal_cost',
       'bmb_expense_personal_cost_detail',
       'bmb_expense_personal_cost_simple', 'bmb_expense_renting_detail',
       'bmb_expense_renting_simple', 'bmb_expense_retail_rental_frq',
       'bmb_expense_retail_rental_per_month',
       'bmb_expense_retail_renting_place',
       'bmb_expense_retail_replenish_cost',
       'bmb_expense_retail_replenish_frq',
       'bmb_expense_service_rental_frq',
       'bmb_expense_service_rental_per_month',
       'bmb_expense_service_renting_place',
       'bmb_expense_service_replenish_cost',
       'bmb_expense_service_replenish_frq',
       'bmb_expense_show_sample_chart',
       'bmb_expense_simple_monthly_operation_cost',
       'bmb_expense_simple_monthly_personal_cost', 'bmb_expense_start',
       'bmb_expense_total', 'bmb_expense_transportation_detail',
       'bmb_expense_yearly_biz_other', 'bmb_expense_yearly_complete',
       'bmb_expense_yearly_donations', 'bmb_expense_yearly_education',
       'bmb_expense_yearly_events', 'bmb_expense_yearly_fees',
       'bmb_expense_yearly_household', 'bmb_expense_yearly_how_prepare',
       'bmb_expense_yearly_medical', 'bmb_expense_yearly_personal_other',
       'bmb_expense_yearly_personal_subtotal',
       'bmb_expense_yearly_personal_type', 'bmb_expense_yearly_repairs',
       'bmb_expense_yearly_start', 'bmb_expense_yearly_subtotal',
       'bmb_intro_biz_confidence', 'bmb_intro_biz_sub_type',
       'bmb_intro_complete', 'bmb_intro_confirmed_complete',
       'bmb_intro_confirmed_settled', 'bmb_intro_confirmed_start',
       'bmb_intro_same_biz', 'bmb_intro_start',
       'bmb_key_partnership_biz_partner',
       'bmb_key_partnership_biz_partner_names',
       'bmb_key_partnership_complete',
       'bmb_key_partnership_ownership_partner_name',
       'bmb_key_partnership_ownership_status',
       'bmb_key_partnership_photo', 'bmb_key_partnership_start',
       'bmb_key_propositions_complete',
       'bmb_key_propositions_opportunity', 'bmb_key_propositions_problem',
       'bmb_key_propositions_start', 'bmb_key_propositions_strength',
       'bmb_key_propositions_threat', 'bmb_key_propositions_value',
       'bmb_key_propositions_weakness', 'bmb_key_resource_category',
       'bmb_key_resource_category_expansion', 'bmb_key_resource_complete',
       'bmb_key_resource_start', 'bmb_revenue_balance_last_month',
       'bmb_revenue_balance_today', 'bmb_revenue_biz_result_check',
       'bmb_revenue_chart_served', 'bmb_revenue_complete',
       'bmb_revenue_how_track', 'bmb_revenue_other_income_have',
       'bmb_revenue_other_income_subtotal', 'bmb_revenue_profit_total',
       'bmb_revenue_revenue_total', 'bmb_revenue_sales_frequency',
       'bmb_revenue_sales_frequency_text', 'bmb_revenue_sales_subtotal',
       'bmb_revenue_sales_total', 'bmb_revenue_seasonality_impact',
       'bmb_revenue_seasonality_worst_season', 'bmb_revenue_start',
       'bmb_revenue_video', 'bmb_revenue_video_quiz_answer',
       'bmb_template_downloaded', 'bmb_template_edit_biz_model',
       'bmb_template_served', 'bmb_update_biz_model_button_clicked',
       'bss_mmod01_bizdiff_coz_external_threat', 'bss_mmod01_cta_start',
       'bss_mmod01_heuristic_start', 'bss_mmod01_hook_start',
       'bss_mmod01_quiz1_to_do_for_financial', 'bss_mmod01_quiz_start',
       'bss_mmod01_skills_start', 'bss_mmod01_started',
       'bss_mmod02_cta_start', 'bss_mmod02_heuristic_start',
       'bss_mmod02_hook_start', 'bss_mmod02_quiz_start',
       'bss_mmod02_skills_start', 'bss_mmod03_cta_start',
       'bss_mmod03_hook_start', 'bss_mmod03_quiz_start',
       'bss_mmod03_skills_start',
       'bss_mmod04_areas_need_to_change_for_biz', 'bss_mmod04_complete',
       'bss_mmod04_cta_start', 'bss_mmod04_customers_demand',
       'bss_mmod04_heuristic_start', 'bss_mmod04_hook_start',
       'bss_mmod04_know_to_handle_dead_biz',
       'bss_mmod04_quiz1_business_operation',
       'bss_mmod04_quiz2_wh_consider_before_change_biz',
       'bss_mmod04_quiz_start', 'bss_mmod04_start', 'bss_mmod05_complete',
       'bss_mmod05_cta_start', 'bss_mmod05_heuristic_start',
       'bss_mmod05_hook_start', 'bss_mmod05_how_manage_biz_practically',
       'bss_mmod05_know_how_manage_biz_for_diff',
       'bss_mmod05_quiz1_products_should_sell',
       'bss_mmod05_quiz2_how_to_manage_staff', 'bss_mmod05_quiz_start',
       'bss_mmod05_skills_start', 'bss_mmod05_start',
       'bss_mmod05_when_start_practically',
       'bss_mmod06_approximate_biz_cost', 'bss_mmod06_complete',
       'bss_mmod06_cta_start', 'bss_mmod06_face_diff_for_biz_operation',
       'bss_mmod06_heuristic_start', 'bss_mmod06_hook_start',
       'bss_mmod06_quiz1_wh_customer_facts_consider',
       'bss_mmod06_quiz2_need_forecast_business_costs',
       'bss_mmod06_quiz_start', 'bss_mmod06_skills_start',
       'bss_mmod06_start', 'bss_mmod1_complete',
       'bss_mmod1_date_start_for_financial_lists',
       'bss_mmod1_how_often_financial_lists',
       'bss_mmod1_quiz2_financial_assess', 'bss_mmod2_complete',
       'bss_mmod2_date_start_for_financial',
       'bss_mmod2_quiz1_areas_reduce_expense',
       'bss_mmod2_quiz2_price_reducing_products_tosell',
       'bss_mmod2_started', 'bss_mmod2_stop_biz_coz_unexpected_conditons',
       'bss_mmod2_what_you_do_for_finance_stability',
       'bss_mmod3_complete', 'bss_mmod3_know_how_change_biz_tocover_diff',
       'bss_mmod3_quiz1_main_function_for_biz', 'bss_mmod3_started',
       'bss_mmod3_what_will_change_for_current_biz',
       'bss_mmod_randomizer', 'bss_mod01_certificate_complete',
       'bss_mod01_certificate_start', 'bss_mod02_certificate_complete',
       'bss_mod02_certificate_start',
       'bss_mod1_mmod01_bizdiff_coz_external_threat',
       'bss_mod1_mmod01_complete', 'bss_mod1_mmod01_cta_start',
       'bss_mod1_mmod01_date_start_for_financial_lists',
       'bss_mod1_mmod01_heuristic_start', 'bss_mod1_mmod01_hook_start',
       'bss_mod1_mmod01_how_often_financial_lists',
       'bss_mod1_mmod01_quiz1_to_do_for_financial',
       'bss_mod1_mmod01_quiz_start', 'bss_mod1_mmod01_skills_start',
       'bss_mod1_mmod01_skills_video_objective', 'bss_mod1_mmod01_start',
       'bss_mod1_mmod02_complete', 'bss_mod1_mmod02_cta_start',
       'bss_mod1_mmod02_date_start_for_financial',
       'bss_mod1_mmod02_heuristic_start', 'bss_mod1_mmod02_hook_start',
       'bss_mod1_mmod02_quiz1_areas_reduce_expense',
       'bss_mod1_mmod02_quiz2_price_reduce_products_tosell',
       'bss_mod1_mmod02_quiz_start', 'bss_mod1_mmod02_skills_start',
       'bss_mod1_mmod02_skills_video_facts', 'bss_mod1_mmod02_start',
       'bss_mod1_mmod02_stop_biz_coz_unexpected_conditons',
       'bss_mod1_mmod02_what_you_do_for_finance_stability',
       'bss_mod1_mmod03_complete', 'bss_mod1_mmod03_cta_start',
       'bss_mod1_mmod03_heuristic_start', 'bss_mod1_mmod03_hook_start',
       'bss_mod1_mmod03_know_how_change_biz_tocover_diff',
       'bss_mod1_mmod03_quiz1_main_function_for_biz',
       'bss_mod1_mmod03_quiz_start', 'bss_mod1_mmod03_skills_start',
       'bss_mod1_mmod03_skills_video_objective', 'bss_mod1_mmod03_start',
       'bss_mod1_mmod03_what_will_change_for_current_biz',
       'bss_mod2_mmod04_areas_need_to_change_for_biz',
       'bss_mod2_mmod04_complete', 'bss_mod2_mmod04_cta_start',
       'bss_mod2_mmod04_customers_demand',
       'bss_mod2_mmod04_heuristic_start', 'bss_mod2_mmod04_hook_start',
       'bss_mod2_mmod04_know_to_handle_dead_biz',
       'bss_mod2_mmod04_quiz1_business_operation',
       'bss_mod2_mmod04_quiz2_wh_consider_before_amend_biz',
       'bss_mod2_mmod04_quiz_start', 'bss_mod2_mmod04_skills_start',
       'bss_mod2_mmod04_skills_video_should_change',
       'bss_mod2_mmod04_start', 'bss_mod2_mmod05_complete',
       'bss_mod2_mmod05_cta_start', 'bss_mod2_mmod05_heuristic_start',
       'bss_mod2_mmod05_hook_start',
       'bss_mod2_mmod05_how_manage_biz_practically',
       'bss_mod2_mmod05_know_how_manage_biz_for_diff',
       'bss_mod2_mmod05_quiz1_products_should_sell',
       'bss_mod2_mmod05_quiz2_how_to_manage_staff',
       'bss_mod2_mmod05_quiz_start', 'bss_mod2_mmod05_skills_start',
       'bss_mod2_mmod05_skills_video_pritorized_products',
       'bss_mod2_mmod05_start', 'bss_mod2_mmod05_when_start_practically',
       'bss_mod2_mmod06_approximate_biz_cost', 'bss_mod2_mmod06_complete',
       'bss_mod2_mmod06_cta_start',
       'bss_mod2_mmod06_face_diff_for_biz_operation',
       'bss_mod2_mmod06_heuristic_start', 'bss_mod2_mmod06_hook_start',
       'bss_mod2_mmod06_quiz1_wh_customer_facts_consider',
       'bss_mod2_mmod06_quiz2_need_forecast_business_costs',
       'bss_mod2_mmod06_quiz_start', 'bss_mod2_mmod06_skills_start',
       'bss_mod2_mmod06_skills_video_steps', 'bss_mod2_mmod06_start',
       'coaching_1.1_complete', 'coaching_1.1_start',
       'coaching_1.1_sv1_ab',
       'coaching_1.1_think_coach_important_forbiz_success',
       'coaching_1.1_think_coach_support_biz',
       'coaching_1.2_broadcast_clicked',
       'coaching_1.2_broadcast_clicked_ab', 'coaching_1.2_start',
       'coaching_2.1_complete', 'coaching_2.1_start',
       'coaching_2.2_complete', 'coaching_2.2_start',
       'coaching_2.3_complete', 'coaching_2.3_start',
       'coaching_3.3_appearance', 'coaching_3.3_appearance_ab',
       'coaching_3.3_appearance_photo', 'coaching_3.3_complete',
       'coaching_3.3_employee_count', 'coaching_3.3_expenses',
       'coaching_3.3_goal_complete', 'coaching_3.3_marketing',
       'coaching_3.3_revenue', 'coaching_3.3_saving_location',
       'coaching_3.3_start', 'coaching_3.3_track_finances',
       'coaching_3.4_score_calculation', 'coaching_3.5_complete',
       'coaching_3.5_start', 'coaching_3.6_OTNR_choice',
       'coaching_3.6_complete', 'coaching_3.6_start',
       'coaching_4.0_complete', 'coaching_4.0_graph_rating',
       'coaching_4.0_score_expectation', 'coaching_4.0_score_url',
       'coaching_4.0_start', 'coaching_4.1_complete',
       'coaching_4.1_counter', 'coaching_4.1_start',
       'coaching_4.3_complete', 'coaching_4.3_start',
       'coaching_5.1_complete', 'coaching_5.1_confirm_ph_number',
       'coaching_5.1_start', 'coaching_5.2_complete',
       'coaching_5.2_start', 'coaching_5.3_average_monthly_profit_2019',
       'coaching_5.3_biz_difficulties_dueto_covid',
       'coaching_5.3_complete', 'coaching_5.3_current_biz_status',
       'coaching_5.3_facts_recover_biz_dueto_covid',
       'coaching_5.3_how_long_current_biz_operate',
       'coaching_5.3_reason_financial_needs',
       'coaching_5.3_reason_less_demand',
       'coaching_5.3_reason_supply_constraints', 'coaching_5.3_start',
       'coaching_5.3_when_biz_will_operate', 'coaching_6.1_complete',
       'coaching_6.1_cta_clicked', 'coaching_6.1_start',
       'coaching_6.2_cta_clicked', 'coaching_6.2_start',
       'coaching_6.3_zigway_cta_application',
       'coaching_6.3_zigway_cta_complete',
       'coaching_6.3_zigway_cta_location',
       'coaching_6.3_zigway_cta_register',
       'coaching_6.3_zigway_cta_served', 'coaching_8.1_complete',
       'coaching_8.1_start', 'coaching_8.2_complete',
       'coaching_8.2_start', 'coaching_ab_testing_A',
       'coaching_ab_testing_B', 'coaching_assigned_staff',
       'coaching_believe_biz_support', 'coaching_best_meeting_day',
       'coaching_best_meeting_time', 'coaching_biz_survive_during_covid',
       'coaching_call_interested', 'coaching_chatbot_lead_source',
       'coaching_coach_feedback', 'coaching_coach_rating',
       'coaching_coach_rating_satisfied', 'coaching_coach_request',
       'coaching_complete', 'coaching_continue_sequence_clicked',
       'coaching_cta_zw1_2_location', 'coaching_cta_zw1_clicked',
       'coaching_cta_zw1_complete', 'coaching_cta_zw1_external_click',
       'coaching_cta_zw1_served', 'coaching_favourite_onow_support',
       'coaching_monthly_goal', 'coaching_monthly_goal_accountability',
       'coaching_monthly_goal_deadline', 'coaching_onow_helped_covid',
       'coaching_onow_student', 'coaching_partner',
       'coaching_partner_unique_id', 'coaching_priority',
       'coaching_session_call_back', 'coaching_session_complete_counter',
       'coaching_session_main_menu_back', 'coaching_session_progress',
       'coaching_session_start_counter', 'coaching_session_unfinished',
       'coaching_session_unfinished_reason',
       'coaching_session_unfinished_served', 'coaching_start',
       'coaching_student_image_url', 'coaching_student_name',
       'coaching_suggest_onow', 'coaching_support_group_url',
       'coaching_update_what_you_wanna_say', 'email', 'factory_worker',
       'gender_confirmed', 'language_pref', 'lead_source', 'location',
       'location_group', 'migrant_status', 'monthly_revenue_graph',
       'myanku_onboarding_complete', 'myanku_onboarding_confirm',
       'myanku_onboarding_family_members',
       'myanku_onboarding_family_members_use',
       'myanku_onboarding_started', 'name', 'onboarding_video_ab_test',
       'onow_program', 'onow_student_id', 'onow_student_id ', 'phone',
       'phone_1', 'phone_2', 'salesforce_business_id',
       'salesforce_contact_id', 'sont_oo_nps', 'source_campaign',
       'startup_cta_complete', 'startup_cta_interested',
       'startup_cta_interested_2', 'startup_cta_interested_3',
       'startup_cta_reason_not_interested',
       'startup_cta_self_identify_biz_owner', 'startup_cta_started',
       'startup_guidline_complete', 'startup_guidline_served',
       'startup_kyc2_complete', 'startup_kyc2_cta_click',
       'startup_kyc2_dependant_number', 'startup_kyc2_education',
       'startup_kyc2_ethinicity', 'startup_kyc2_income_range',
       'startup_kyc2_income_user_input', 'startup_kyc2_marital_status',
       'startup_kyc2_occupation_status', 'startup_kyc2_specific_job_type',
       'startup_kyc2_start', 'startup_lesson01_complete',
       'startup_lesson01_cta_biz_name', 'startup_lesson01_cta_photo',
       'startup_lesson01_heuristic_complete',
       'startup_lesson01_hook_define_biz_type',
       'startup_lesson01_quiz1_answer',
       'startup_lesson01_skills_2ndtime_video',
       'startup_lesson01_skills_image_click',
       'startup_lesson01_skills_video_answer', 'startup_lesson01_start',
       'startup_lesson02_complete',
       'startup_lesson02_cta_business_ethics',
       'startup_lesson02_cta_value_community',
       'startup_lesson02_heuristic_complete',
       'startup_lesson02_hook_unworthy_price_product',
       'startup_lesson02_quiz1_answer',
       'startup_lesson02_skills_image_click',
       'startup_lesson02_skills_video_answer', 'startup_lesson02_start',
       'startup_lesson03_complete', 'startup_lesson03_cta_image_click',
       'startup_lesson03_heuristic_complete',
       'startup_lesson03_hook_plan_before_biz',
       'startup_lesson03_quiz1_answer', 'startup_lesson03_quiz2_answer',
       'startup_lesson03_skills_image_click',
       'startup_lesson03_skills_video_answer', 'startup_lesson03_start',
       'startup_lesson04_complete',
       'startup_lesson04_cta_customer_age_group',
       'startup_lesson04_cta_customer_income',
       'startup_lesson04_heuristic_complete',
       'startup_lesson04_hook_study_customer_needs',
       'startup_lesson04_quiz1_answer', 'startup_lesson04_quiz2_answer',
       'startup_lesson04_skills_image_click',
       'startup_lesson04_skills_video_answer', 'startup_lesson04_start',
       'startup_lesson05_complete',
       'startup_lesson05_cta_customer_solution',
       'startup_lesson05_heuristic_complete',
       'startup_lesson05_hook_studied_swot_before',
       'startup_lesson05_quiz1_answer', 'startup_lesson05_quiz2_answer',
       'startup_lesson05_skills_2ndtime_video',
       'startup_lesson05_skills_image_click',
       'startup_lesson05_skills_video_answer', 'startup_lesson05_start',
       'startup_lesson06_complete',
       'startup_lesson06_cta_marketing_method',
       'startup_lesson06_heuristic_complete',
       'startup_lesson06_hook_customer_awareness',
       'startup_lesson06_quiz1_answer', 'startup_lesson06_quiz2_answer',
       'startup_lesson06_skills_2ndtime_video',
       'startup_lesson06_skills_image_click',
       'startup_lesson06_skills_video_answer', 'startup_lesson06_start',
       'startup_lesson07_complete',
       'startup_lesson07_cta_build_customer_relation',
       'startup_lesson07_heuristic_complete',
       'startup_lesson07_hook_customer_relation',
       'startup_lesson07_quiz1_answer', 'startup_lesson07_quiz2_answer',
       'startup_lesson07_skills_image_click',
       'startup_lesson07_skills_video_answer', 'startup_lesson07_start',
       'startup_lesson08_complete', 'startup_lesson08_cta_biz_resources',
       'startup_lesson08_cta_important_partners',
       'startup_lesson08_heuristic_complete',
       'startup_lesson08_hook_need_biz_partners',
       'startup_lesson08_quiz1_answer',
       'startup_lesson08_skills_image_click',
       'startup_lesson08_skills_video_answer', 'startup_lesson08_start',
       'startup_lesson09_complete', 'startup_lesson09_cta_image_click',
       'startup_lesson09_cta_important_biz_need',
       'startup_lesson09_heurisitc_complete',
       'startup_lesson09_hook_time_management',
       'startup_lesson09_quiz1_answer', 'startup_lesson09_quiz2_answer',
       'startup_lesson09_skills_image_click',
       'startup_lesson09_skills_video_answer', 'startup_lesson09_start',
       'startup_lesson10_complete', 'startup_lesson10_heuristic_complete',
       'startup_lesson10_hook_think_before_spent',
       'startup_lesson10_quiz1_answer', 'startup_lesson10_quiz2_answer',
       'startup_lesson10_skills_image_click',
       'startup_lesson10_skills_video_answer', 'startup_lesson10_start',
       'startup_lesson11_complete', 'startup_lesson11_cta_served',
       'startup_lesson11_heuristic_complete',
       'startup_lesson11_hook_calculate_expense',
       'startup_lesson11_quiz1_answer', 'startup_lesson11_quiz2_answer',
       'startup_lesson11_skills_image_click',
       'startup_lesson11_skills_video_answer', 'startup_lesson11_start',
       'startup_lesson12_complete', 'startup_lesson12_cta_served',
       'startup_lesson12_heuristic_complete',
       'startup_lesson12_hook_track_record',
       'startup_lesson12_quiz1_answer', 'startup_lesson12_quiz2_answer',
       'startup_lesson12_skills_image_click',
       'startup_lesson12_skills_video_answer', 'startup_lesson12_start',
       'startup_main_menu_served', 'startup_mod01_complete',
       'startup_mod01_served', 'startup_mod02_complete',
       'startup_mod02_served', 'startup_mod03_served',
       'startup_online_course_benefit', 'startup_online_course_intro',
       'startup_online_interest', 'startup_online_register_age',
       'startup_online_register_complete',
       'startup_online_register_current_position',
       'startup_online_register_intro',
       'startup_online_register_location', 'startup_online_register_name',
       'startup_online_register_nrc', 'startup_online_section_complete',
       'startup_online_section_intro', 'testing',
       'vps_signup_confirm_already_joined_fb',
       'vps_signup_confirm_bss_click', 'vps_signup_confirm_complete',
       'vps_signup_confirm_join_fb_now', 'vps_signup_confirm_served',
       'vps_signup_confirm_video_clicked', 'welcome_complete',
       'welcome_language_ab', 'welcome_star', 'welcome_start'],
      dtype=object)
>>> import json
>>> json.dump(list(le.classes_), open('classes_.json', 'w'))
>>> more classes_.json
>>> !clear
>>> df.columns
Index(['id', 'messenger_id', 'attribute', 'value', 'timestamp',
       'attribute_num'],
      dtype='object')
>>> df.drop(columns=['attribute'])
              id      messenger_id                     value             timestamp  attribute_num
0        3961076  3866330546752060                         4  2021-01-09T06:26:46Z            319
1        3961077  3866330546752060                         4  2021-01-09T06:26:46Z            313
2        3961078  3866330546752060                         5  2021-01-09T06:26:46Z            320
3        3961079  3866330546752060                         2  2021-01-09T06:26:46Z            324
4        3961081  3866330546752060             Upper Myanmar  2021-01-09T06:26:46Z            420
...          ...               ...                       ...                   ...            ...
4319311  3961072  3866330546752060  စိုက်ပျိုးရေးလုပ်ကိုင်တာ  2021-01-09T06:26:46Z              7
4319312  3961073  3866330546752060                    Stable  2021-01-09T06:26:46Z              5
4319313  3961074  3866330546752060                      TRUE  2021-01-09T06:26:46Z            307
4319314  3961075  3866330546752060                      TRUE  2021-01-09T06:26:46Z            323
4319315  3961041  3426199597492758                         2  2021-01-09T06:26:46Z            322

[4319316 rows x 5 columns]
>>> df
              id      messenger_id  ...             timestamp attribute_num
0        3961076  3866330546752060  ...  2021-01-09T06:26:46Z           319
1        3961077  3866330546752060  ...  2021-01-09T06:26:46Z           313
2        3961078  3866330546752060  ...  2021-01-09T06:26:46Z           320
3        3961079  3866330546752060  ...  2021-01-09T06:26:46Z           324
4        3961081  3866330546752060  ...  2021-01-09T06:26:46Z           420
...          ...               ...  ...                   ...           ...
4319311  3961072  3866330546752060  ...  2021-01-09T06:26:46Z             7
4319312  3961073  3866330546752060  ...  2021-01-09T06:26:46Z             5
4319313  3961074  3866330546752060  ...  2021-01-09T06:26:46Z           307
4319314  3961075  3866330546752060  ...  2021-01-09T06:26:46Z           323
4319315  3961041  3426199597492758  ...  2021-01-09T06:26:46Z           322

[4319316 rows x 6 columns]
>>> df.columns
Index(['id', 'messenger_id', 'attribute', 'value', 'timestamp',
       'attribute_num'],
      dtype='object')
>>> import this
>>> df
              id      messenger_id  ...             timestamp attribute_num
0        3961076  3866330546752060  ...  2021-01-09T06:26:46Z           319
1        3961077  3866330546752060  ...  2021-01-09T06:26:46Z           313
2        3961078  3866330546752060  ...  2021-01-09T06:26:46Z           320
3        3961079  3866330546752060  ...  2021-01-09T06:26:46Z           324
4        3961081  3866330546752060  ...  2021-01-09T06:26:46Z           420
...          ...               ...  ...                   ...           ...
4319311  3961072  3866330546752060  ...  2021-01-09T06:26:46Z             7
4319312  3961073  3866330546752060  ...  2021-01-09T06:26:46Z             5
4319313  3961074  3866330546752060  ...  2021-01-09T06:26:46Z           307
4319314  3961075  3866330546752060  ...  2021-01-09T06:26:46Z           323
4319315  3961041  3426199597492758  ...  2021-01-09T06:26:46Z           322

[4319316 rows x 6 columns]
>>> df.columns
Index(['id', 'messenger_id', 'attribute', 'value', 'timestamp',
       'attribute_num'],
      dtype='object')
>>> df = df.drop(columns=['attribute'])
>>> df.columns
Index(['id', 'messenger_id', 'value', 'timestamp', 'attribute_num'], dtype='object')
>>> df.drop(columns=['attribute_num'])
              id      messenger_id                     value             timestamp
0        3961076  3866330546752060                         4  2021-01-09T06:26:46Z
1        3961077  3866330546752060                         4  2021-01-09T06:26:46Z
2        3961078  3866330546752060                         5  2021-01-09T06:26:46Z
3        3961079  3866330546752060                         2  2021-01-09T06:26:46Z
4        3961081  3866330546752060             Upper Myanmar  2021-01-09T06:26:46Z
...          ...               ...                       ...                   ...
4319311  3961072  3866330546752060  စိုက်ပျိုးရေးလုပ်ကိုင်တာ  2021-01-09T06:26:46Z
4319312  3961073  3866330546752060                    Stable  2021-01-09T06:26:46Z
4319313  3961074  3866330546752060                      TRUE  2021-01-09T06:26:46Z
4319314  3961075  3866330546752060                      TRUE  2021-01-09T06:26:46Z
4319315  3961041  3426199597492758                         2  2021-01-09T06:26:46Z

[4319316 rows x 4 columns]
>>> df.columns
Index(['id', 'messenger_id', 'value', 'timestamp', 'attribute_num'], dtype='object')
>>> !clear
>>> users = pd.read_csv('onow_chatbot_user_tangible.csv.gz'
... )
...
>>> users.columns
Index(['id', 'messenger_id', 'first_name', 'last_name', 'name', 'gender',
       'phone', 'timezone', 'locale', 'source_campaign', 'testing',
       'coaching_session_start_counter', 'coaching_session_complete_counter',
       'language_pref', 'biz_owner', 'startup_online_interest',
       'coaching_onow_student', 'onow_id', 'gender_confirmed', 'birth_year',
       'location_group', 'location', 'phone_2', 'migrant_status',
       'coaching_3_6_otnr_choice', 'coaching_support_group_url', 'user_photo',
       'coaching_assigned_staff', 'coaching_call_interested'],
      dtype='object')
>>> del users
>>> !clear
>>> ls -al
>>> df
              id      messenger_id                     value             timestamp  attribute_num
0        3961076  3866330546752060                         4  2021-01-09T06:26:46Z            319
1        3961077  3866330546752060                         4  2021-01-09T06:26:46Z            313
2        3961078  3866330546752060                         5  2021-01-09T06:26:46Z            320
3        3961079  3866330546752060                         2  2021-01-09T06:26:46Z            324
4        3961081  3866330546752060             Upper Myanmar  2021-01-09T06:26:46Z            420
...          ...               ...                       ...                   ...            ...
4319311  3961072  3866330546752060  စိုက်ပျိုးရေးလုပ်ကိုင်တာ  2021-01-09T06:26:46Z              7
4319312  3961073  3866330546752060                    Stable  2021-01-09T06:26:46Z              5
4319313  3961074  3866330546752060                      TRUE  2021-01-09T06:26:46Z            307
4319314  3961075  3866330546752060                      TRUE  2021-01-09T06:26:46Z            323
4319315  3961041  3426199597492758                         2  2021-01-09T06:26:46Z            322

[4319316 rows x 5 columns]
>>> le.classes_
array(['birth_year', 'biz_dead_covid', 'biz_dead_date_closed',
       'biz_dead_goals', 'biz_dead_reason', 'biz_health_status',
       'biz_industry', 'biz_name', 'biz_owner', 'biz_paused_covid_reason',
       'biz_paused_date_paused', 'biz_paused_notes', 'biz_paused_reason',
       'biz_paused_when_reopen', 'biz_pivot_covid', 'biz_pivot_date',
       'biz_pivot_new_industry', 'biz_pivot_new_name', 'biz_pivot_notes',
       'biz_pivot_reason', 'bizsur_mmod1_status', 'bizsur_mmod2_status',
       'bizsur_mmod3_status', 'bizsur_mmod4_status',
       'bizsur_mmod5_status', 'bizsur_mmod6_status', 'bizsur_mod1_status',
       'bizsur_mod2_status', 'bizsur_status', 'bmb_channels_complete',
       'bmb_channels_primary_acquisition',
       'bmb_channels_primary_delivery', 'bmb_channels_start',
       'bmb_cr_complete', 'bmb_cr_product_customers_count',
       'bmb_cr_products_per_customer', 'bmb_cr_return',
       'bmb_cr_service_customers_count', 'bmb_cr_services_per_customer',
       'bmb_cr_start', 'bmb_cr_style', 'bmb_customer_segments_age',
       'bmb_customer_segments_complete', 'bmb_customer_segments_gender',
       'bmb_customer_segments_location',
       'bmb_customer_segments_special_interest',
       'bmb_customer_segments_start', 'bmb_expense_complete',
       'bmb_expense_daily_food_cost', 'bmb_expense_employee_detail',
       'bmb_expense_have_maintainence_cost',
       'bmb_expense_having_employees', 'bmb_expense_inventory_inputs',
       'bmb_expense_inventory_inputs_detail',
       'bmb_expense_inventory_inputs_simple', 'bmb_expense_irregular',
       'bmb_expense_marketing_detail',
       'bmb_expense_monthly_employee_cost',
       'bmb_expense_monthly_general_cost',
       'bmb_expense_monthly_health_cost',
       'bmb_expense_monthly_maintainence_cost',
       'bmb_expense_monthly_marketing_cost',
       'bmb_expense_monthly_other_operation_cost',
       'bmb_expense_monthly_transport_cost',
       'bmb_expense_operation_cost_detail',
       'bmb_expense_operation_cost_simple',
       'bmb_expense_option_to_observe', 'bmb_expense_other_personal_cost',
       'bmb_expense_personal_cost_detail',
       'bmb_expense_personal_cost_simple', 'bmb_expense_renting_detail',
       'bmb_expense_renting_simple', 'bmb_expense_retail_rental_frq',
       'bmb_expense_retail_rental_per_month',
       'bmb_expense_retail_renting_place',
       'bmb_expense_retail_replenish_cost',
       'bmb_expense_retail_replenish_frq',
       'bmb_expense_service_rental_frq',
       'bmb_expense_service_rental_per_month',
       'bmb_expense_service_renting_place',
       'bmb_expense_service_replenish_cost',
       'bmb_expense_service_replenish_frq',
       'bmb_expense_show_sample_chart',
       'bmb_expense_simple_monthly_operation_cost',
       'bmb_expense_simple_monthly_personal_cost', 'bmb_expense_start',
       'bmb_expense_total', 'bmb_expense_transportation_detail',
       'bmb_expense_yearly_biz_other', 'bmb_expense_yearly_complete',
       'bmb_expense_yearly_donations', 'bmb_expense_yearly_education',
       'bmb_expense_yearly_events', 'bmb_expense_yearly_fees',
       'bmb_expense_yearly_household', 'bmb_expense_yearly_how_prepare',
       'bmb_expense_yearly_medical', 'bmb_expense_yearly_personal_other',
       'bmb_expense_yearly_personal_subtotal',
       'bmb_expense_yearly_personal_type', 'bmb_expense_yearly_repairs',
       'bmb_expense_yearly_start', 'bmb_expense_yearly_subtotal',
       'bmb_intro_biz_confidence', 'bmb_intro_biz_sub_type',
       'bmb_intro_complete', 'bmb_intro_confirmed_complete',
       'bmb_intro_confirmed_settled', 'bmb_intro_confirmed_start',
       'bmb_intro_same_biz', 'bmb_intro_start',
       'bmb_key_partnership_biz_partner',
       'bmb_key_partnership_biz_partner_names',
       'bmb_key_partnership_complete',
       'bmb_key_partnership_ownership_partner_name',
       'bmb_key_partnership_ownership_status',
       'bmb_key_partnership_photo', 'bmb_key_partnership_start',
       'bmb_key_propositions_complete',
       'bmb_key_propositions_opportunity', 'bmb_key_propositions_problem',
       'bmb_key_propositions_start', 'bmb_key_propositions_strength',
       'bmb_key_propositions_threat', 'bmb_key_propositions_value',
       'bmb_key_propositions_weakness', 'bmb_key_resource_category',
       'bmb_key_resource_category_expansion', 'bmb_key_resource_complete',
       'bmb_key_resource_start', 'bmb_revenue_balance_last_month',
       'bmb_revenue_balance_today', 'bmb_revenue_biz_result_check',
       'bmb_revenue_chart_served', 'bmb_revenue_complete',
       'bmb_revenue_how_track', 'bmb_revenue_other_income_have',
       'bmb_revenue_other_income_subtotal', 'bmb_revenue_profit_total',
       'bmb_revenue_revenue_total', 'bmb_revenue_sales_frequency',
       'bmb_revenue_sales_frequency_text', 'bmb_revenue_sales_subtotal',
       'bmb_revenue_sales_total', 'bmb_revenue_seasonality_impact',
       'bmb_revenue_seasonality_worst_season', 'bmb_revenue_start',
       'bmb_revenue_video', 'bmb_revenue_video_quiz_answer',
       'bmb_template_downloaded', 'bmb_template_edit_biz_model',
       'bmb_template_served', 'bmb_update_biz_model_button_clicked',
       'bss_mmod01_bizdiff_coz_external_threat', 'bss_mmod01_cta_start',
       'bss_mmod01_heuristic_start', 'bss_mmod01_hook_start',
       'bss_mmod01_quiz1_to_do_for_financial', 'bss_mmod01_quiz_start',
       'bss_mmod01_skills_start', 'bss_mmod01_started',
       'bss_mmod02_cta_start', 'bss_mmod02_heuristic_start',
       'bss_mmod02_hook_start', 'bss_mmod02_quiz_start',
       'bss_mmod02_skills_start', 'bss_mmod03_cta_start',
       'bss_mmod03_hook_start', 'bss_mmod03_quiz_start',
       'bss_mmod03_skills_start',
       'bss_mmod04_areas_need_to_change_for_biz', 'bss_mmod04_complete',
       'bss_mmod04_cta_start', 'bss_mmod04_customers_demand',
       'bss_mmod04_heuristic_start', 'bss_mmod04_hook_start',
       'bss_mmod04_know_to_handle_dead_biz',
       'bss_mmod04_quiz1_business_operation',
       'bss_mmod04_quiz2_wh_consider_before_change_biz',
       'bss_mmod04_quiz_start', 'bss_mmod04_start', 'bss_mmod05_complete',
       'bss_mmod05_cta_start', 'bss_mmod05_heuristic_start',
       'bss_mmod05_hook_start', 'bss_mmod05_how_manage_biz_practically',
       'bss_mmod05_know_how_manage_biz_for_diff',
       'bss_mmod05_quiz1_products_should_sell',
       'bss_mmod05_quiz2_how_to_manage_staff', 'bss_mmod05_quiz_start',
       'bss_mmod05_skills_start', 'bss_mmod05_start',
       'bss_mmod05_when_start_practically',
       'bss_mmod06_approximate_biz_cost', 'bss_mmod06_complete',
       'bss_mmod06_cta_start', 'bss_mmod06_face_diff_for_biz_operation',
       'bss_mmod06_heuristic_start', 'bss_mmod06_hook_start',
       'bss_mmod06_quiz1_wh_customer_facts_consider',
       'bss_mmod06_quiz2_need_forecast_business_costs',
       'bss_mmod06_quiz_start', 'bss_mmod06_skills_start',
       'bss_mmod06_start', 'bss_mmod1_complete',
       'bss_mmod1_date_start_for_financial_lists',
       'bss_mmod1_how_often_financial_lists',
       'bss_mmod1_quiz2_financial_assess', 'bss_mmod2_complete',
       'bss_mmod2_date_start_for_financial',
       'bss_mmod2_quiz1_areas_reduce_expense',
       'bss_mmod2_quiz2_price_reducing_products_tosell',
       'bss_mmod2_started', 'bss_mmod2_stop_biz_coz_unexpected_conditons',
       'bss_mmod2_what_you_do_for_finance_stability',
       'bss_mmod3_complete', 'bss_mmod3_know_how_change_biz_tocover_diff',
       'bss_mmod3_quiz1_main_function_for_biz', 'bss_mmod3_started',
       'bss_mmod3_what_will_change_for_current_biz',
       'bss_mmod_randomizer', 'bss_mod01_certificate_complete',
       'bss_mod01_certificate_start', 'bss_mod02_certificate_complete',
       'bss_mod02_certificate_start',
       'bss_mod1_mmod01_bizdiff_coz_external_threat',
       'bss_mod1_mmod01_complete', 'bss_mod1_mmod01_cta_start',
       'bss_mod1_mmod01_date_start_for_financial_lists',
       'bss_mod1_mmod01_heuristic_start', 'bss_mod1_mmod01_hook_start',
       'bss_mod1_mmod01_how_often_financial_lists',
       'bss_mod1_mmod01_quiz1_to_do_for_financial',
       'bss_mod1_mmod01_quiz_start', 'bss_mod1_mmod01_skills_start',
       'bss_mod1_mmod01_skills_video_objective', 'bss_mod1_mmod01_start',
       'bss_mod1_mmod02_complete', 'bss_mod1_mmod02_cta_start',
       'bss_mod1_mmod02_date_start_for_financial',
       'bss_mod1_mmod02_heuristic_start', 'bss_mod1_mmod02_hook_start',
       'bss_mod1_mmod02_quiz1_areas_reduce_expense',
       'bss_mod1_mmod02_quiz2_price_reduce_products_tosell',
       'bss_mod1_mmod02_quiz_start', 'bss_mod1_mmod02_skills_start',
       'bss_mod1_mmod02_skills_video_facts', 'bss_mod1_mmod02_start',
       'bss_mod1_mmod02_stop_biz_coz_unexpected_conditons',
       'bss_mod1_mmod02_what_you_do_for_finance_stability',
       'bss_mod1_mmod03_complete', 'bss_mod1_mmod03_cta_start',
       'bss_mod1_mmod03_heuristic_start', 'bss_mod1_mmod03_hook_start',
       'bss_mod1_mmod03_know_how_change_biz_tocover_diff',
       'bss_mod1_mmod03_quiz1_main_function_for_biz',
       'bss_mod1_mmod03_quiz_start', 'bss_mod1_mmod03_skills_start',
       'bss_mod1_mmod03_skills_video_objective', 'bss_mod1_mmod03_start',
       'bss_mod1_mmod03_what_will_change_for_current_biz',
       'bss_mod2_mmod04_areas_need_to_change_for_biz',
       'bss_mod2_mmod04_complete', 'bss_mod2_mmod04_cta_start',
       'bss_mod2_mmod04_customers_demand',
       'bss_mod2_mmod04_heuristic_start', 'bss_mod2_mmod04_hook_start',
       'bss_mod2_mmod04_know_to_handle_dead_biz',
       'bss_mod2_mmod04_quiz1_business_operation',
       'bss_mod2_mmod04_quiz2_wh_consider_before_amend_biz',
       'bss_mod2_mmod04_quiz_start', 'bss_mod2_mmod04_skills_start',
       'bss_mod2_mmod04_skills_video_should_change',
       'bss_mod2_mmod04_start', 'bss_mod2_mmod05_complete',
       'bss_mod2_mmod05_cta_start', 'bss_mod2_mmod05_heuristic_start',
       'bss_mod2_mmod05_hook_start',
       'bss_mod2_mmod05_how_manage_biz_practically',
       'bss_mod2_mmod05_know_how_manage_biz_for_diff',
       'bss_mod2_mmod05_quiz1_products_should_sell',
       'bss_mod2_mmod05_quiz2_how_to_manage_staff',
       'bss_mod2_mmod05_quiz_start', 'bss_mod2_mmod05_skills_start',
       'bss_mod2_mmod05_skills_video_pritorized_products',
       'bss_mod2_mmod05_start', 'bss_mod2_mmod05_when_start_practically',
       'bss_mod2_mmod06_approximate_biz_cost', 'bss_mod2_mmod06_complete',
       'bss_mod2_mmod06_cta_start',
       'bss_mod2_mmod06_face_diff_for_biz_operation',
       'bss_mod2_mmod06_heuristic_start', 'bss_mod2_mmod06_hook_start',
       'bss_mod2_mmod06_quiz1_wh_customer_facts_consider',
       'bss_mod2_mmod06_quiz2_need_forecast_business_costs',
       'bss_mod2_mmod06_quiz_start', 'bss_mod2_mmod06_skills_start',
       'bss_mod2_mmod06_skills_video_steps', 'bss_mod2_mmod06_start',
       'coaching_1.1_complete', 'coaching_1.1_start',
       'coaching_1.1_sv1_ab',
       'coaching_1.1_think_coach_important_forbiz_success',
       'coaching_1.1_think_coach_support_biz',
       'coaching_1.2_broadcast_clicked',
       'coaching_1.2_broadcast_clicked_ab', 'coaching_1.2_start',
       'coaching_2.1_complete', 'coaching_2.1_start',
       'coaching_2.2_complete', 'coaching_2.2_start',
       'coaching_2.3_complete', 'coaching_2.3_start',
       'coaching_3.3_appearance', 'coaching_3.3_appearance_ab',
       'coaching_3.3_appearance_photo', 'coaching_3.3_complete',
       'coaching_3.3_employee_count', 'coaching_3.3_expenses',
       'coaching_3.3_goal_complete', 'coaching_3.3_marketing',
       'coaching_3.3_revenue', 'coaching_3.3_saving_location',
       'coaching_3.3_start', 'coaching_3.3_track_finances',
       'coaching_3.4_score_calculation', 'coaching_3.5_complete',
       'coaching_3.5_start', 'coaching_3.6_OTNR_choice',
       'coaching_3.6_complete', 'coaching_3.6_start',
       'coaching_4.0_complete', 'coaching_4.0_graph_rating',
       'coaching_4.0_score_expectation', 'coaching_4.0_score_url',
       'coaching_4.0_start', 'coaching_4.1_complete',
       'coaching_4.1_counter', 'coaching_4.1_start',
       'coaching_4.3_complete', 'coaching_4.3_start',
       'coaching_5.1_complete', 'coaching_5.1_confirm_ph_number',
       'coaching_5.1_start', 'coaching_5.2_complete',
       'coaching_5.2_start', 'coaching_5.3_average_monthly_profit_2019',
       'coaching_5.3_biz_difficulties_dueto_covid',
       'coaching_5.3_complete', 'coaching_5.3_current_biz_status',
       'coaching_5.3_facts_recover_biz_dueto_covid',
       'coaching_5.3_how_long_current_biz_operate',
       'coaching_5.3_reason_financial_needs',
       'coaching_5.3_reason_less_demand',
       'coaching_5.3_reason_supply_constraints', 'coaching_5.3_start',
       'coaching_5.3_when_biz_will_operate', 'coaching_6.1_complete',
       'coaching_6.1_cta_clicked', 'coaching_6.1_start',
       'coaching_6.2_cta_clicked', 'coaching_6.2_start',
       'coaching_6.3_zigway_cta_application',
       'coaching_6.3_zigway_cta_complete',
       'coaching_6.3_zigway_cta_location',
       'coaching_6.3_zigway_cta_register',
       'coaching_6.3_zigway_cta_served', 'coaching_8.1_complete',
       'coaching_8.1_start', 'coaching_8.2_complete',
       'coaching_8.2_start', 'coaching_ab_testing_A',
       'coaching_ab_testing_B', 'coaching_assigned_staff',
       'coaching_believe_biz_support', 'coaching_best_meeting_day',
       'coaching_best_meeting_time', 'coaching_biz_survive_during_covid',
       'coaching_call_interested', 'coaching_chatbot_lead_source',
       'coaching_coach_feedback', 'coaching_coach_rating',
       'coaching_coach_rating_satisfied', 'coaching_coach_request',
       'coaching_complete', 'coaching_continue_sequence_clicked',
       'coaching_cta_zw1_2_location', 'coaching_cta_zw1_clicked',
       'coaching_cta_zw1_complete', 'coaching_cta_zw1_external_click',
       'coaching_cta_zw1_served', 'coaching_favourite_onow_support',
       'coaching_monthly_goal', 'coaching_monthly_goal_accountability',
       'coaching_monthly_goal_deadline', 'coaching_onow_helped_covid',
       'coaching_onow_student', 'coaching_partner',
       'coaching_partner_unique_id', 'coaching_priority',
       'coaching_session_call_back', 'coaching_session_complete_counter',
       'coaching_session_main_menu_back', 'coaching_session_progress',
       'coaching_session_start_counter', 'coaching_session_unfinished',
       'coaching_session_unfinished_reason',
       'coaching_session_unfinished_served', 'coaching_start',
       'coaching_student_image_url', 'coaching_student_name',
       'coaching_suggest_onow', 'coaching_support_group_url',
       'coaching_update_what_you_wanna_say', 'email', 'factory_worker',
       'gender_confirmed', 'language_pref', 'lead_source', 'location',
       'location_group', 'migrant_status', 'monthly_revenue_graph',
       'myanku_onboarding_complete', 'myanku_onboarding_confirm',
       'myanku_onboarding_family_members',
       'myanku_onboarding_family_members_use',
       'myanku_onboarding_started', 'name', 'onboarding_video_ab_test',
       'onow_program', 'onow_student_id', 'onow_student_id ', 'phone',
       'phone_1', 'phone_2', 'salesforce_business_id',
       'salesforce_contact_id', 'sont_oo_nps', 'source_campaign',
       'startup_cta_complete', 'startup_cta_interested',
       'startup_cta_interested_2', 'startup_cta_interested_3',
       'startup_cta_reason_not_interested',
       'startup_cta_self_identify_biz_owner', 'startup_cta_started',
       'startup_guidline_complete', 'startup_guidline_served',
       'startup_kyc2_complete', 'startup_kyc2_cta_click',
       'startup_kyc2_dependant_number', 'startup_kyc2_education',
       'startup_kyc2_ethinicity', 'startup_kyc2_income_range',
       'startup_kyc2_income_user_input', 'startup_kyc2_marital_status',
       'startup_kyc2_occupation_status', 'startup_kyc2_specific_job_type',
       'startup_kyc2_start', 'startup_lesson01_complete',
       'startup_lesson01_cta_biz_name', 'startup_lesson01_cta_photo',
       'startup_lesson01_heuristic_complete',
       'startup_lesson01_hook_define_biz_type',
       'startup_lesson01_quiz1_answer',
       'startup_lesson01_skills_2ndtime_video',
       'startup_lesson01_skills_image_click',
       'startup_lesson01_skills_video_answer', 'startup_lesson01_start',
       'startup_lesson02_complete',
       'startup_lesson02_cta_business_ethics',
       'startup_lesson02_cta_value_community',
       'startup_lesson02_heuristic_complete',
       'startup_lesson02_hook_unworthy_price_product',
       'startup_lesson02_quiz1_answer',
       'startup_lesson02_skills_image_click',
       'startup_lesson02_skills_video_answer', 'startup_lesson02_start',
       'startup_lesson03_complete', 'startup_lesson03_cta_image_click',
       'startup_lesson03_heuristic_complete',
       'startup_lesson03_hook_plan_before_biz',
       'startup_lesson03_quiz1_answer', 'startup_lesson03_quiz2_answer',
       'startup_lesson03_skills_image_click',
       'startup_lesson03_skills_video_answer', 'startup_lesson03_start',
       'startup_lesson04_complete',
       'startup_lesson04_cta_customer_age_group',
       'startup_lesson04_cta_customer_income',
       'startup_lesson04_heuristic_complete',
       'startup_lesson04_hook_study_customer_needs',
       'startup_lesson04_quiz1_answer', 'startup_lesson04_quiz2_answer',
       'startup_lesson04_skills_image_click',
       'startup_lesson04_skills_video_answer', 'startup_lesson04_start',
       'startup_lesson05_complete',
       'startup_lesson05_cta_customer_solution',
       'startup_lesson05_heuristic_complete',
       'startup_lesson05_hook_studied_swot_before',
       'startup_lesson05_quiz1_answer', 'startup_lesson05_quiz2_answer',
       'startup_lesson05_skills_2ndtime_video',
       'startup_lesson05_skills_image_click',
       'startup_lesson05_skills_video_answer', 'startup_lesson05_start',
       'startup_lesson06_complete',
       'startup_lesson06_cta_marketing_method',
       'startup_lesson06_heuristic_complete',
       'startup_lesson06_hook_customer_awareness',
       'startup_lesson06_quiz1_answer', 'startup_lesson06_quiz2_answer',
       'startup_lesson06_skills_2ndtime_video',
       'startup_lesson06_skills_image_click',
       'startup_lesson06_skills_video_answer', 'startup_lesson06_start',
       'startup_lesson07_complete',
       'startup_lesson07_cta_build_customer_relation',
       'startup_lesson07_heuristic_complete',
       'startup_lesson07_hook_customer_relation',
       'startup_lesson07_quiz1_answer', 'startup_lesson07_quiz2_answer',
       'startup_lesson07_skills_image_click',
       'startup_lesson07_skills_video_answer', 'startup_lesson07_start',
       'startup_lesson08_complete', 'startup_lesson08_cta_biz_resources',
       'startup_lesson08_cta_important_partners',
       'startup_lesson08_heuristic_complete',
       'startup_lesson08_hook_need_biz_partners',
       'startup_lesson08_quiz1_answer',
       'startup_lesson08_skills_image_click',
       'startup_lesson08_skills_video_answer', 'startup_lesson08_start',
       'startup_lesson09_complete', 'startup_lesson09_cta_image_click',
       'startup_lesson09_cta_important_biz_need',
       'startup_lesson09_heurisitc_complete',
       'startup_lesson09_hook_time_management',
       'startup_lesson09_quiz1_answer', 'startup_lesson09_quiz2_answer',
       'startup_lesson09_skills_image_click',
       'startup_lesson09_skills_video_answer', 'startup_lesson09_start',
       'startup_lesson10_complete', 'startup_lesson10_heuristic_complete',
       'startup_lesson10_hook_think_before_spent',
       'startup_lesson10_quiz1_answer', 'startup_lesson10_quiz2_answer',
       'startup_lesson10_skills_image_click',
       'startup_lesson10_skills_video_answer', 'startup_lesson10_start',
       'startup_lesson11_complete', 'startup_lesson11_cta_served',
       'startup_lesson11_heuristic_complete',
       'startup_lesson11_hook_calculate_expense',
       'startup_lesson11_quiz1_answer', 'startup_lesson11_quiz2_answer',
       'startup_lesson11_skills_image_click',
       'startup_lesson11_skills_video_answer', 'startup_lesson11_start',
       'startup_lesson12_complete', 'startup_lesson12_cta_served',
       'startup_lesson12_heuristic_complete',
       'startup_lesson12_hook_track_record',
       'startup_lesson12_quiz1_answer', 'startup_lesson12_quiz2_answer',
       'startup_lesson12_skills_image_click',
       'startup_lesson12_skills_video_answer', 'startup_lesson12_start',
       'startup_main_menu_served', 'startup_mod01_complete',
       'startup_mod01_served', 'startup_mod02_complete',
       'startup_mod02_served', 'startup_mod03_served',
       'startup_online_course_benefit', 'startup_online_course_intro',
       'startup_online_interest', 'startup_online_register_age',
       'startup_online_register_complete',
       'startup_online_register_current_position',
       'startup_online_register_intro',
       'startup_online_register_location', 'startup_online_register_name',
       'startup_online_register_nrc', 'startup_online_section_complete',
       'startup_online_section_intro', 'testing',
       'vps_signup_confirm_already_joined_fb',
       'vps_signup_confirm_bss_click', 'vps_signup_confirm_complete',
       'vps_signup_confirm_join_fb_now', 'vps_signup_confirm_served',
       'vps_signup_confirm_video_clicked', 'welcome_complete',
       'welcome_language_ab', 'welcome_star', 'welcome_start'],
      dtype=object)
>>> [c for c in le.classes_ if 'profit' in c.lower()]
['bmb_revenue_profit_total', 'coaching_5.3_average_monthly_profit_2019']
>>> [i, c for (i, c) in enumerate(le.classes_) if 'profit' in c.lower()]
>>> [(i, c) for (i, c) in enumerate(le.classes_) if 'profit' in c.lower()]
[(138, 'bmb_revenue_profit_total'),
 (346, 'coaching_5.3_average_monthly_profit_2019')]
>>> profit = df['value'][df['attribute_num'] == 138]
>>> profit
42399       7000000
42855      -8300000
44139         50000
44813        265000
44907         10000
             ...   
4257463         -64
4270315      -50000
4274731         -64
4275448     -400000
4300270    -1010000
Name: value, Length: 1055, dtype: object
>>> timestamp = df['timestamp'][profit.index]
>>> len(timestamp)
1055
>>> len(profit)
1055
>>> df_profit = pd.DataFrame([timestamp, profit])
>>> df_profit
                        42399                 42855    ...               4275448               4300270
timestamp  2021-01-13T05:35:40Z  2021-01-13T06:49:17Z  ...  2021-01-07T16:38:22Z  2021-01-09T06:26:23Z
value                   7000000              -8300000  ...               -400000              -1010000

[2 rows x 1055 columns]
>>> df_profit = df_profit.T
>>> df_profit
                    timestamp     value
42399    2021-01-13T05:35:40Z   7000000
42855    2021-01-13T06:49:17Z  -8300000
44139    2021-01-13T10:07:59Z     50000
44813    2021-01-13T11:13:50Z    265000
44907    2021-01-13T11:19:43Z     10000
...                       ...       ...
4257463  2021-01-05T16:34:06Z       -64
4270315  2021-01-07T06:09:44Z    -50000
4274731  2021-01-07T15:12:10Z       -64
4275448  2021-01-07T16:38:22Z   -400000
4300270  2021-01-09T06:26:23Z  -1010000

[1055 rows x 2 columns]
>>> df_profit['timestamp']
42399      2021-01-13T05:35:40Z
42855      2021-01-13T06:49:17Z
44139      2021-01-13T10:07:59Z
44813      2021-01-13T11:13:50Z
44907      2021-01-13T11:19:43Z
                   ...         
4257463    2021-01-05T16:34:06Z
4270315    2021-01-07T06:09:44Z
4274731    2021-01-07T15:12:10Z
4275448    2021-01-07T16:38:22Z
4300270    2021-01-09T06:26:23Z
Name: timestamp, Length: 1055, dtype: object
>>> df_profit['timestamp'][0]
>>> df_profit['timestamp'].iloc[0]
'2021-01-13T05:35:40Z'
>>> df_profit['timestamp'] = pd.to_datetime(df_profit['timestamp'])
>>> df_profit['timestamp'].iloc[0]
Timestamp('2021-01-13 05:35:40+0000', tz='UTC')
>>> df_profit['timestamp'].year
>>> df_profit['timestamp'].iloc[0].year
2021
>>> df_profit['timestamp'].dt.year
42399      2021
42855      2021
44139      2021
44813      2021
44907      2021
           ... 
4257463    2021
4270315    2021
4274731    2021
4275448    2021
4300270    2021
Name: timestamp, Length: 1055, dtype: int64
>>> df_profit['timestamp'].str.len()
>>> df_profit['year'] = df_profit['timestamp'].dt.year
>>> df_profit['month'] = df_profit['timestamp'].dt.month
>>> df_profit['weekday'] = df_profit['timestamp'].dt.weekday
>>> df_profit.descibe()
>>> df_profit.describe()
              year        month      weekday
count  1055.000000  1055.000000  1055.000000
mean   2020.977251     1.357346     3.179147
std       0.149172     1.666810     1.522488
min    2020.000000     1.000000     0.000000
25%    2021.000000     1.000000     2.000000
50%    2021.000000     1.000000     3.000000
75%    2021.000000     1.000000     4.000000
max    2021.000000    12.000000     6.000000
>>> df_profit.columns
Index(['timestamp', 'value', 'year', 'month', 'weekday'], dtype='object')
>>> df_profit['value_str_len'] = df_profit['value'].str.len()
>>> df_profit['value_num'] = df_profit['value'].atype(int)
>>> df_profit['value_num'] = df_profit['value'].astype(int)
>>> df_profit['value_num'] = df_profit['value'].astype(float)
>>> from sklearn.linear_model import LinearRegression, Lasso, Ridge
>>> model = LinearRegression()
>>> feature_names = ['month']
>>> target_names = ['value_str_len', 'value_num']
>>> model.fit(df_profit[feature_names], df_profit[target_names])
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)
>>> y_train_pred = model.predict(df_profit[feature_names])
>>> y_train_pred
array([[6.19196455e+00, 2.97442557e+92],
       [6.19196455e+00, 2.97442557e+92],
       [6.19196455e+00, 2.97442557e+92],
       ...,
       [6.19196455e+00, 2.97442557e+92],
       [6.19196455e+00, 2.97442557e+92],
       [6.19196455e+00, 2.97442557e+92]])
>>> pd.get_dummies(df_profit, columns=feature_names)
                        timestamp     value  year  weekday  ...  month_1  month_2  month_3  month_12
42399   2021-01-13 05:35:40+00:00   7000000  2021        2  ...        1        0        0         0
42855   2021-01-13 06:49:17+00:00  -8300000  2021        2  ...        1        0        0         0
44139   2021-01-13 10:07:59+00:00     50000  2021        2  ...        1        0        0         0
44813   2021-01-13 11:13:50+00:00    265000  2021        2  ...        1        0        0         0
44907   2021-01-13 11:19:43+00:00     10000  2021        2  ...        1        0        0         0
...                           ...       ...   ...      ...  ...      ...      ...      ...       ...
4257463 2021-01-05 16:34:06+00:00       -64  2021        1  ...        1        0        0         0
4270315 2021-01-07 06:09:44+00:00    -50000  2021        3  ...        1        0        0         0
4274731 2021-01-07 15:12:10+00:00       -64  2021        3  ...        1        0        0         0
4275448 2021-01-07 16:38:22+00:00   -400000  2021        3  ...        1        0        0         0
4300270 2021-01-09 06:26:23+00:00  -1010000  2021        5  ...        1        0        0         0

[1055 rows x 10 columns]
>>> pd.get_dummies(df_profit, columns=feature_names).columns
Index(['timestamp', 'value', 'year', 'weekday', 'value_str_len', 'value_num',
       'month_1', 'month_2', 'month_3', 'month_12'],
      dtype='object')
>>> df_profit.columns
Index(['timestamp', 'value', 'year', 'month', 'weekday', 'value_str_len',
       'value_num'],
      dtype='object')
>>> df_profit
                        timestamp     value  year  month  weekday  value_str_len  value_num
42399   2021-01-13 05:35:40+00:00   7000000  2021      1        2              7  7000000.0
42855   2021-01-13 06:49:17+00:00  -8300000  2021      1        2              8 -8300000.0
44139   2021-01-13 10:07:59+00:00     50000  2021      1        2              5    50000.0
44813   2021-01-13 11:13:50+00:00    265000  2021      1        2              6   265000.0
44907   2021-01-13 11:19:43+00:00     10000  2021      1        2              5    10000.0
...                           ...       ...   ...    ...      ...            ...        ...
4257463 2021-01-05 16:34:06+00:00       -64  2021      1        1              3      -64.0
4270315 2021-01-07 06:09:44+00:00    -50000  2021      1        3              6   -50000.0
4274731 2021-01-07 15:12:10+00:00       -64  2021      1        3              3      -64.0
4275448 2021-01-07 16:38:22+00:00   -400000  2021      1        3              7  -400000.0
4300270 2021-01-09 06:26:23+00:00  -1010000  2021      1        5              8 -1010000.0

[1055 rows x 7 columns]
>>> type(pd.get_dummies(df_profit, columns=feature_names))
pandas.core.frame.DataFrame
>>> df_profit
                        timestamp     value  year  month  weekday  value_str_len  value_num
42399   2021-01-13 05:35:40+00:00   7000000  2021      1        2              7  7000000.0
42855   2021-01-13 06:49:17+00:00  -8300000  2021      1        2              8 -8300000.0
44139   2021-01-13 10:07:59+00:00     50000  2021      1        2              5    50000.0
44813   2021-01-13 11:13:50+00:00    265000  2021      1        2              6   265000.0
44907   2021-01-13 11:19:43+00:00     10000  2021      1        2              5    10000.0
...                           ...       ...   ...    ...      ...            ...        ...
4257463 2021-01-05 16:34:06+00:00       -64  2021      1        1              3      -64.0
4270315 2021-01-07 06:09:44+00:00    -50000  2021      1        3              6   -50000.0
4274731 2021-01-07 15:12:10+00:00       -64  2021      1        3              3      -64.0
4275448 2021-01-07 16:38:22+00:00   -400000  2021      1        3              7  -400000.0
4300270 2021-01-09 06:26:23+00:00  -1010000  2021      1        5              8 -1010000.0

[1055 rows x 7 columns]
>>> pd.get_dummies(df_profit, columns=feature_names)
                        timestamp     value  year  weekday  ...  month_1  month_2  month_3  month_12
42399   2021-01-13 05:35:40+00:00   7000000  2021        2  ...        1        0        0         0
42855   2021-01-13 06:49:17+00:00  -8300000  2021        2  ...        1        0        0         0
44139   2021-01-13 10:07:59+00:00     50000  2021        2  ...        1        0        0         0
44813   2021-01-13 11:13:50+00:00    265000  2021        2  ...        1        0        0         0
44907   2021-01-13 11:19:43+00:00     10000  2021        2  ...        1        0        0         0
...                           ...       ...   ...      ...  ...      ...      ...      ...       ...
4257463 2021-01-05 16:34:06+00:00       -64  2021        1  ...        1        0        0         0
4270315 2021-01-07 06:09:44+00:00    -50000  2021        3  ...        1        0        0         0
4274731 2021-01-07 15:12:10+00:00       -64  2021        3  ...        1        0        0         0
4275448 2021-01-07 16:38:22+00:00   -400000  2021        3  ...        1        0        0         0
4300270 2021-01-09 06:26:23+00:00  -1010000  2021        5  ...        1        0        0         0

[1055 rows x 10 columns]
>>> df_profit = pd.get_dummies(df_profit, columns=feature_names)
>>> df_profit
                        timestamp     value  year  weekday  ...  month_1  month_2  month_3  month_12
42399   2021-01-13 05:35:40+00:00   7000000  2021        2  ...        1        0        0         0
42855   2021-01-13 06:49:17+00:00  -8300000  2021        2  ...        1        0        0         0
44139   2021-01-13 10:07:59+00:00     50000  2021        2  ...        1        0        0         0
44813   2021-01-13 11:13:50+00:00    265000  2021        2  ...        1        0        0         0
44907   2021-01-13 11:19:43+00:00     10000  2021        2  ...        1        0        0         0
...                           ...       ...   ...      ...  ...      ...      ...      ...       ...
4257463 2021-01-05 16:34:06+00:00       -64  2021        1  ...        1        0        0         0
4270315 2021-01-07 06:09:44+00:00    -50000  2021        3  ...        1        0        0         0
4274731 2021-01-07 15:12:10+00:00       -64  2021        3  ...        1        0        0         0
4275448 2021-01-07 16:38:22+00:00   -400000  2021        3  ...        1        0        0         0
4300270 2021-01-09 06:26:23+00:00  -1010000  2021        5  ...        1        0        0         0

[1055 rows x 10 columns]
>>> feature_names
['month']
>>> feature_names = [c for c in df_profit.columns if 'month_' in c]
>>> feature_names
['month_1', 'month_2', 'month_3', 'month_12']
>>> feature_names = [c for c in df_profit.columns if c.startswith('month_')]
>>> model.fit(df_profit[feature_names], df_profit[target_names])
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)
>>> y_train_pred = model.predict(df_profit[feature_names])
>>> y_train_pred
array([[6.18384697e+00, 3.18809777e+92],
       [6.18384697e+00, 3.18809777e+92],
       [6.18384697e+00, 3.18809777e+92],
       ...,
       [6.18384697e+00, 3.18809777e+92],
       [6.18384697e+00, 3.18809777e+92],
       [6.18384697e+00, 3.18809777e+92]])
>>> model = Ridge()
>>> model.fit(df_profit[feature_names], df_profit[target_names])
Ridge(alpha=1.0, copy_X=True, fit_intercept=True, max_iter=None,
      normalize=False, random_state=None, solver='auto', tol=0.001)
>>> y_train_pred = model.predict(df_profit[feature_names])
>>> y_train_pred
array([[6.18391554e+00, 3.18557968e+92],
       [6.18391554e+00, 3.18557968e+92],
       [6.18391554e+00, 3.18557968e+92],
       ...,
       [6.18391554e+00, 3.18557968e+92],
       [6.18391554e+00, 3.18557968e+92],
       [6.18391554e+00, 3.18557968e+92]])
>>> df_profit.sum()
value            7000000-8300000500002650001000026500050000-100...
year                                                       2132131
weekday                                                       3354
value_str_len                                                 6531
value_num                                                    3e+95
month_1                                                        941
month_2                                                         67
month_3                                                         23
month_12                                                        24
dtype: object
>>> df_profit = pd.get_dummies(df_profit, columns=['year'])
>>> df_profit.sum()
value            7000000-8300000500002650001000026500050000-100...
weekday                                                       3354
value_str_len                                                 6531
value_num                                                    3e+95
month_1                                                        941
month_2                                                         67
month_3                                                         23
month_12                                                        24
year_2020                                                       24
year_2021                                                     1031
dtype: object
>>> target_name
>>> target_names
['value_str_len', 'value_num']
>>> df_profit.describe()
           weekday  value_str_len     value_num      month_1  ...      month_3     month_12    year_2020    year_2021
count  1055.000000    1055.000000  1.055000e+03  1055.000000  ...  1055.000000  1055.000000  1055.000000  1055.000000
mean      3.179147       6.190521  2.843602e+92     0.891943  ...     0.021801     0.022749     0.022749     0.977251
std       1.522488       1.562944  9.236236e+93     0.310599  ...     0.146102     0.149172     0.149172     0.149172
min       0.000000       1.000000 -1.000000e+31     0.000000  ...     0.000000     0.000000     0.000000     0.000000
25%       2.000000       6.000000 -1.825000e+05     1.000000  ...     0.000000     0.000000     0.000000     1.000000
50%       3.000000       6.000000 -3.200000e+01     1.000000  ...     0.000000     0.000000     0.000000     1.000000
75%       4.000000       7.000000  1.500000e+05     1.000000  ...     0.000000     0.000000     0.000000     1.000000
max       6.000000      15.000000  3.000000e+95     1.000000  ...     1.000000     1.000000     1.000000     1.000000

[8 rows x 9 columns]
>>> df_profit['value_num'] = df_profit['value_num'][df_profit['value_num'] < 1e94]
>>> df_profit.describe()
           weekday  value_str_len     value_num      month_1  ...      month_3     month_12    year_2020    year_2021
count  1055.000000    1055.000000  1.054000e+03  1055.000000  ...  1055.000000  1055.000000  1055.000000  1055.000000
mean      3.179147       6.190521 -9.487666e+27     0.891943  ...     0.021801     0.022749     0.022749     0.977251
std       1.522488       1.562944  3.080206e+29     0.310599  ...     0.146102     0.149172     0.149172     0.149172
min       0.000000       1.000000 -1.000000e+31     0.000000  ...     0.000000     0.000000     0.000000     0.000000
25%       2.000000       6.000000 -1.837500e+05     1.000000  ...     0.000000     0.000000     0.000000     1.000000
50%       3.000000       6.000000 -4.250000e+01     1.000000  ...     0.000000     0.000000     0.000000     1.000000
75%       4.000000       7.000000  1.500000e+05     1.000000  ...     0.000000     0.000000     0.000000     1.000000
max       6.000000      15.000000  1.800000e+13     1.000000  ...     1.000000     1.000000     1.000000     1.000000

[8 rows x 9 columns]
>>> df_profit['value_num'] = df_profit['value_num'][df_profit['value_num'].abs() < 1e30]
>>> df_profit
                        timestamp     value  weekday  value_str_len  ...  month_3  month_12  year_2020  year_2021
42399   2021-01-13 05:35:40+00:00   7000000        2              7  ...        0         0          0          1
42855   2021-01-13 06:49:17+00:00  -8300000        2              8  ...        0         0          0          1
44139   2021-01-13 10:07:59+00:00     50000        2              5  ...        0         0          0          1
44813   2021-01-13 11:13:50+00:00    265000        2              6  ...        0         0          0          1
44907   2021-01-13 11:19:43+00:00     10000        2              5  ...        0         0          0          1
...                           ...       ...      ...            ...  ...      ...       ...        ...        ...
4257463 2021-01-05 16:34:06+00:00       -64        1              3  ...        0         0          0          1
4270315 2021-01-07 06:09:44+00:00    -50000        3              6  ...        0         0          0          1
4274731 2021-01-07 15:12:10+00:00       -64        3              3  ...        0         0          0          1
4275448 2021-01-07 16:38:22+00:00   -400000        3              7  ...        0         0          0          1
4300270 2021-01-09 06:26:23+00:00  -1010000        5              8  ...        0         0          0          1

[1055 rows x 11 columns]
>>> df_profit.describe()
           weekday  value_str_len     value_num      month_1  ...      month_3     month_12    year_2020    year_2021
count  1055.000000    1055.000000  1.053000e+03  1055.000000  ...  1055.000000  1055.000000  1055.000000  1055.000000
mean      3.179147       6.190521  1.748357e+10     0.891943  ...     0.021801     0.022749     0.022749     0.977251
std       1.522488       1.562944  5.547408e+11     0.310599  ...     0.146102     0.149172     0.149172     0.149172
min       0.000000       1.000000 -2.512050e+10     0.000000  ...     0.000000     0.000000     0.000000     0.000000
25%       2.000000       6.000000 -1.800000e+05     1.000000  ...     0.000000     0.000000     0.000000     1.000000
50%       3.000000       6.000000 -3.200000e+01     1.000000  ...     0.000000     0.000000     0.000000     1.000000
75%       4.000000       7.000000  1.500000e+05     1.000000  ...     0.000000     0.000000     0.000000     1.000000
max       6.000000      15.000000  1.800000e+13     1.000000  ...     1.000000     1.000000     1.000000     1.000000

[8 rows x 9 columns]
>>> len(df_profit)
1055
>>> model.fit(df_profit[feature_names], df_profit[target_names])
>>> target_names
['value_str_len', 'value_num']
>>> df_profit.describe()
           weekday  value_str_len     value_num      month_1  ...      month_3     month_12    year_2020    year_2021
count  1055.000000    1055.000000  1.053000e+03  1055.000000  ...  1055.000000  1055.000000  1055.000000  1055.000000
mean      3.179147       6.190521  1.748357e+10     0.891943  ...     0.021801     0.022749     0.022749     0.977251
std       1.522488       1.562944  5.547408e+11     0.310599  ...     0.146102     0.149172     0.149172     0.149172
min       0.000000       1.000000 -2.512050e+10     0.000000  ...     0.000000     0.000000     0.000000     0.000000
25%       2.000000       6.000000 -1.800000e+05     1.000000  ...     0.000000     0.000000     0.000000     1.000000
50%       3.000000       6.000000 -3.200000e+01     1.000000  ...     0.000000     0.000000     0.000000     1.000000
75%       4.000000       7.000000  1.500000e+05     1.000000  ...     0.000000     0.000000     0.000000     1.000000
max       6.000000      15.000000  1.800000e+13     1.000000  ...     1.000000     1.000000     1.000000     1.000000

[8 rows x 9 columns]
>>> pd.options.display.max_columns = 10000
>>> df_profit.describe()
           weekday  value_str_len     value_num      month_1      month_2  \
count  1055.000000    1055.000000  1.053000e+03  1055.000000  1055.000000   
mean      3.179147       6.190521  1.748357e+10     0.891943     0.063507   
std       1.522488       1.562944  5.547408e+11     0.310599     0.243988   
min       0.000000       1.000000 -2.512050e+10     0.000000     0.000000   
25%       2.000000       6.000000 -1.800000e+05     1.000000     0.000000   
50%       3.000000       6.000000 -3.200000e+01     1.000000     0.000000   
75%       4.000000       7.000000  1.500000e+05     1.000000     0.000000   
max       6.000000      15.000000  1.800000e+13     1.000000     1.000000   

           month_3     month_12    year_2020    year_2021  
count  1055.000000  1055.000000  1055.000000  1055.000000  
mean      0.021801     0.022749     0.022749     0.977251  
std       0.146102     0.149172     0.149172     0.149172  
min       0.000000     0.000000     0.000000     0.000000  
25%       0.000000     0.000000     0.000000     1.000000  
50%       0.000000     0.000000     0.000000     1.000000  
75%       0.000000     0.000000     0.000000     1.000000  
max       1.000000     1.000000     1.000000     1.000000  
>>> df_profit.dropna()
                        timestamp     value  weekday  value_str_len  \
42399   2021-01-13 05:35:40+00:00   7000000        2              7   
42855   2021-01-13 06:49:17+00:00  -8300000        2              8   
44139   2021-01-13 10:07:59+00:00     50000        2              5   
44813   2021-01-13 11:13:50+00:00    265000        2              6   
44907   2021-01-13 11:19:43+00:00     10000        2              5   
...                           ...       ...      ...            ...   
4257463 2021-01-05 16:34:06+00:00       -64        1              3   
4270315 2021-01-07 06:09:44+00:00    -50000        3              6   
4274731 2021-01-07 15:12:10+00:00       -64        3              3   
4275448 2021-01-07 16:38:22+00:00   -400000        3              7   
4300270 2021-01-09 06:26:23+00:00  -1010000        5              8   

         value_num  month_1  month_2  month_3  month_12  year_2020  year_2021  
42399    7000000.0        1        0        0         0          0          1  
42855   -8300000.0        1        0        0         0          0          1  
44139      50000.0        1        0        0         0          0          1  
44813     265000.0        1        0        0         0          0          1  
44907      10000.0        1        0        0         0          0          1  
...            ...      ...      ...      ...       ...        ...        ...  
4257463      -64.0        1        0        0         0          0          1  
4270315   -50000.0        1        0        0         0          0          1  
4274731      -64.0        1        0        0         0          0          1  
4275448  -400000.0        1        0        0         0          0          1  
4300270 -1010000.0        1        0        0         0          0          1  

[1053 rows x 11 columns]
>>> df_profit = df_profit.dropna()
>>> model.fit(df_profit[feature_names], df_profit[target_names])
Ridge(alpha=1.0, copy_X=True, fit_intercept=True, max_iter=None,
      normalize=False, random_state=None, solver='auto', tol=0.001)
>>> y_train_pred = model.predict(df_profit[feature_names])
>>> y_train_pred
array([[6.17366575e+00, 1.95110304e+10],
       [6.17366575e+00, 1.95110304e+10],
       [6.17366575e+00, 1.95110304e+10],
       ...,
       [6.17366575e+00, 1.95110304e+10],
       [6.17366575e+00, 1.95110304e+10],
       [6.17366575e+00, 1.95110304e+10]])
>>> ls
>>> echo "" >> numericize_attributes.py
>>> !echo "" >> numericize_attributes.py
>>> !echo "" >> numericize_attributes.py
>>> !echo '"""' >> numericize_attributes.py
>>> history -o -p -f numericize_attributes_mobsession.md
"""
