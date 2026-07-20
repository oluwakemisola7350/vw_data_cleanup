
CREATE VIEW vw_data_cleaned AS (
	SELECT 
		l.pk,
		COALESCE(l.sk, 'Unknown/No_Id') sk, 
		p.pk pk_opp,
		p.opportunity_id,
		COALESCE(l.assigned_cohort, 'Unknown') assigned_cohort, 
		COALESCE(CAST(CASE WHEN l.fee ~ '^[0-9.]+$' THEN l.fee ELSE '0.0' END AS FLOAT), 0.0) fee,
		COALESCE(CAST(
	      CASE 
	         WHEN l.status ~ '^[0-9.]+$' THEN SPLIT_PART(l.status, '.', 1)
	         ELSE '0' END AS BIGINT), 0) status,
			 COALESCE(sm."Status", 'Unknown'
			 		  ) accept_reject_status,
		CASE 
	        WHEN l.accept_reject_date IS NULL OR l.accept_reject_date = '' THEN NULL 
	        WHEN l.accept_reject_date LIKE '%-%' THEN LEFT(l.accept_reject_date, 10)::date
	        WHEN l.accept_reject_date ~ '^[0-9]+$' THEN to_timestamp(CAST(l.accept_reject_date AS BIGINT) / 1000.0)::date 
	        ELSE NULL
	    END AS accept_reject_date,
		CASE WHEN l.accept_reject_date IS NULL OR l.accept_reject_date = '' THEN 'Pending Decision' ELSE 'Decided' END accept_reject_decision_status,
		COALESCE(CAST(
	       CASE 
	         WHEN l.amount_to_be_paid ~ '^[0-9.]+$' THEN SPLIT_PART(l.amount_to_be_paid, '.', 1) ELSE '0' END AS BIGINT), 0) amount_to_be_paid,
		COALESCE(l.transaction_id, 'Unknown/No Id') transaction_id,
		COALESCE(l.payment_status, 'Unknown') payment_status, 
		COALESCE(l.i_agree_to_terms_and_conditions_of_global_shala, 'Unknown') agreement_to_terms,
		CASE 
	        WHEN l.modified_at IS NULL OR l.modified_at = '' THEN NULL
	        WHEN l.modified_at LIKE '%-%' THEN LEFT(l.modified_at, 10)::date 
	        WHEN SPLIT_PART(l.modified_at, '.', 1) ~ '^[0-9]+$' 
	        THEN to_timestamp(CAST(SPLIT_PART(l.modified_at, '.', 1) AS BIGINT) / 1000.0)::date 
	        ELSE NULL 
	    END AS modified_at,
		CASE WHEN l.modified_at IS NULL OR l.modified_at = '' THEN 'Original Record' ELSE 'Modified' END Modified_Status,
		l.apply_date,
		CASE WHEN l.apply_date IS NULL OR l.apply_date = '' THEN 'Incomplete' ELSE 'Applied' END Apply_Status,
		COALESCE(from_where_did_you_hear_about_us, 'Unknown Source') referral_source,
		COALESCE(l.accept_reject_reason, 'Unknown Reason') accept_reject_reason, 
		COALESCE(l.category, 'Unknown') category, 
		CASE 
	        WHEN l.not_started_date IS NULL OR l.not_started_date = '' THEN NULL
	        WHEN l.not_started_date LIKE '%-%' THEN LEFT(l.not_started_date, 10)::date 
	        WHEN SPLIT_PART(l.modified_at, '.', 1) ~ '^[0-9]+$' 
	        THEN to_timestamp(CAST(SPLIT_PART(l.not_started_date, '.', 1) AS BIGINT) / 1000.0)::date 
	        ELSE NULL 
	    END not_started_date, 
		CASE WHEN l.not_started_date IS NULL OR l.not_started_date = '' THEN 'Started' ELSE 'Not Started' END start_status,
		COALESCE(l.cohort_p2, 'Unknown') cohort2, 
		COALESCE(l.cohort_p1, 'Unknown') cohort1,
		COALESCE(l.relation_id, 'Unknown') relation_id, 
		CASE 
	        WHEN l.reward_awarded_date IS NULL OR l.reward_awarded_date = '' THEN NULL
	        WHEN l.reward_awarded_date LIKE '%-%' THEN LEFT(l.reward_awarded_date, 10)::date 
	        WHEN SPLIT_PART(l.reward_awarded_date, '.', 1) ~ '^[0-9]+$' 
	        THEN to_timestamp(CAST(SPLIT_PART(l.reward_awarded_date, '.', 1) AS BIGINT) / 1000.0)::date 
	        ELSE NULL 
	    END reward_awarded_date,
		CASE WHEN l.reward_awarded_date IS NULL OR l.reward_awarded_date = '' THEN 'Not Awarded' ELSE 'Awarded' END reward_award_status,
		CASE 
	        WHEN l.completion_date IS NULL OR l.completion_date = '' THEN NULL
	        WHEN l.completion_date LIKE '%-%' THEN LEFT(l.completion_date, 10)::date 
	        WHEN SPLIT_PART(completion_date, '.', 1) ~ '^[0-9]+$' 
	        THEN to_timestamp(CAST(SPLIT_PART(l.completion_date, '.', 1) AS BIGINT) / 1000.0)::date 
	        ELSE NULL
			END completion_date,
		CASE WHEN l.completion_date IS NULL OR l.completion_date = '' THEN 'In Progress' ELSE 'Completed' END completion_status,
		COALESCE(l.withdraw_reason, 'Unknown Reason') withdraw_reason,
		COALESCE(l.team_name, 'Unknown') team_name, 
		COALESCE(l.team_code, 'Unknown') team_code, 
		COALESCE(l.application_id, 'Unknown') application_id, 
		COALESCE(l.i_have_read_and_agreed_to_the_terms_and_conditions, 'False') agreed_to_terms,
		COALESCE(l.team_creator, 'No Team Creator') team_creator,
		COALESCE(l.send_for_approval_mechanism_t_c, 'Not Sent') approval_method,
		COALESCE(l.please_identify_your_student_status, 'Not Specified') please_identify_your_student_status,
		COALESCE(l.i_understand_that_i_will_have_to_commit_at_least56_hours_each_w, 'False') hours_committed_ok,
		COALESCE(l.why_do_you_want_to_apply_for_this_internship1, 'Not Specified') application_reason1,
		COALESCE(l.i_will_be_available_from79_pm_ist730930_am_cst_for_meetings_onc, 'False') meetings_available,
		COALESCE(l.from_which_medium_did_you_hear_about_the_internship, 'Not Specified') referral_source, 
		COALESCE(l.why_do_you_want_to_apply_for_this_internship, 'Not Specified') internship_application_reason2,
		CASE 
	        WHEN l.withdraw_date IS NULL OR l.withdraw_date = '' THEN NULL 
	        WHEN l.withdraw_date LIKE '%-%' AND LEFT(l.withdraw_date,1) != '{' THEN LEFT(withdraw_date, 10)::date 
	        WHEN SPLIT_PART(l.withdraw_date, '.', 1) ~ '^[0-9]+$' 
	        THEN to_timestamp(CAST(SPLIT_PART(l.withdraw_date, '.', 1) AS BIGINT) / 1000.0)::date 
	        ELSE NULL
	    END withdraw_date, 
		CASE WHEN l.withdraw_date IS NULL OR l.withdraw_date = '' THEN 'Enrolled' ELSE 'Withdrawn' END withdraw_status, 
		CASE 
	        WHEN l.created_at IS NULL OR l.created_at = '' THEN NULL
	        WHEN l.created_at LIKE '%-%' AND LEFT(l.created_at,1) != '{' THEN LEFT(l.created_at, 10)::date 
	        WHEN SPLIT_PART(l.created_at, '.', 1) ~ '^[0-9]+$' 
	        THEN to_timestamp(CAST(SPLIT_PART(l.created_at, '.', 1) AS BIGINT) / 1000.0)::date 
	        ELSE NULL 
	    END created_at, 
		CASE WHEN l.created_at IS NULL OR l.created_at = '' THEN 'Draft' ELSE 'Registered' END created_at_status,
		COALESCE(l.external_reference_url, 'No Link Provided') external_reference_url,
		COALESCE(l.work_item_sk, 'Unknown') work_item_sk,
		COALESCE(l.i_understand_that_this_is_the_first_step_towards_my_application, 'False') agreed_first_step,
		COALESCE(l.how_did_you_hear_about_this_opportunity, 'Not Specified') referral_source_opportunity,
		COALESCE(l.can_you_share_an_experience_where_you_proactively_pursued_learn, 'No Response Provided') Proactive_learning_essay,
		CASE 
	        WHEN l.dropped_out_date IS NULL OR l.dropped_out_date = '' THEN NULL
	        WHEN l.dropped_out_date LIKE '%-%' AND LEFT(l.dropped_out_date ,1) != '{' THEN LEFT(l.dropped_out_date, 10)::date 
	        WHEN SPLIT_PART(l.dropped_out_date, '.', 1) ~ '^[0-9]+$' 
	        THEN to_timestamp(CAST(SPLIT_PART(l.dropped_out_date, '.', 1) AS BIGINT) / 1000.0)::date 
	        ELSE NULL 
	    END dropped_out_date,
		CASE WHEN l.dropped_out_date IS NULL THEN 'Active' ELSE 'Dropped Out' END drop_out_status,
		COALESCE(l.appear_in_wishlist, 'False') appear_in_wishlist,
			COALESCE(p."Badge", 'Unknown') badge_opp, 
		COALESCE(p."CareerAddOn", 'Unknown') carrer_add_on_opp, 
		COALESCE(p.code, 'Unknown') code_opp, 
		COALESCE(p."Cohort", 'Unknown') cohort_opp,
		COALESCE(p.fee, 'Unknown') fee_opp,
		COALESCE(p.currency_type, 'Unknown') currency_type_opp,
		COALESCE(p.current_editor, 'Unknown')  current_editor_opp,
		COALESCE(p."DropoutTransaction", 'Unknown') dropout_transaction_opp, 
		COALESCE(CAST(p.duration AS INT), 0) duration_opp, 
		COALESCE(p.duration_type, 'Unknown') duration_type_opp, 
		COALESCE(p."Eligibility", 'Unknown') eligibility_opp, 
		COALESCE(CAST(p.fee AS INT), 0) fee_opp, 
		COALESCE(p.image_link, 'No Link') image_link_opp, 
		COALESCE(p.is_archived, 'False') is_archived_opp,
		COALESCE(p.is_auto_approve, 'Unknown') is_auto_approve_opp,
		CASE 
	        WHEN p.last_date_to_apply IS NULL OR p.last_date_to_apply = '' THEN NULL
	        WHEN p.last_date_to_apply LIKE '%-%' AND LEFT(p.last_date_to_apply,1) != '{' THEN LEFT(p.last_date_to_apply, 10)::date 
	        WHEN SPLIT_PART(p.last_date_to_apply, '.', 1) ~ '^[0-9]+$' 
	        THEN to_timestamp(CAST(SPLIT_PART(p.last_date_to_apply, '.', 1) AS BIGINT) / 1000.0)::date 
	        ELSE NULL 
	    END last_date_to_apply, 
		COAlESCE(p.location, 'Unknown') location_opp, 
		COALESCE(p.long_description, 'No Description') long_description, 
		COALESCE(p.microscholarship, 'Unknown') microscholarship, 
		COALESCE(p.name, 'No Name') name, 
		COALESCE(p."NotStartedTransaction", 'Unknown') not_started_transaction, 
		COALESCE(p."Panellist", 'Unknown') panellist, 
		COALESCE(p."Reward", 'No Reward') reward, 
		COALESCE(p.role, 'Unknown') role, 
		COALESCE(p.role_responsibility, 'Unknown') role_responsibility,
		COALESCE(p.short_description, 'No Description') short_description,   
		COALESCE(p.summary, 'Unknown') summary, 
		COALESCE(p."Testimonial", 'Unknown') testimonial, 
		COALESCE(p.tracking_questions, 'No Traching Question') tracking_question
		FROM public.learner_dataset l
		LEFT JOIN status_mapping sm
		ON sm."Status Code" = 	COALESCE(CAST(
	                                       CASE 
	                                          WHEN l.status ~ '^[0-9.]+$' THEN SPLIT_PART(l.status, '.', 1)
	                                          ELSE '0' END AS BIGINT), 0)
		LEFT JOIN opportunity_dataset p
		ON p.category = COALESCE(l.category, 'Unknown')
) 
