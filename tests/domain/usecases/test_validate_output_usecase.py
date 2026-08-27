from domain.usecases.validate_output_usecase import ValidateOutputUseCase


def test_flags_claim_not_present_in_source_context():
    usecase = ValidateOutputUseCase()

    result = usecase.execute(
        output="I worked at Google Brasil for 5 anos.",
        source_context="Ana worked as a software engineer.",
    )

    assert result.is_grounded is False
    assert "Google Brasil" in result.flagged_claims
    assert "5 anos" in result.flagged_claims


def test_does_not_flag_claims_present_in_source_context():
    usecase = ValidateOutputUseCase()

    result = usecase.execute(
        output="Ana worked at Google Brasil.",
        source_context="Ana worked at Google Brasil for several years.",
    )

    assert result.is_grounded is True
    assert result.flagged_claims == []


def test_no_specific_claims_extracted_is_considered_grounded():
    usecase = ValidateOutputUseCase()

    result = usecase.execute(
        output="she has strong communication skills.",
        source_context="",
    )

    assert result.is_grounded is True
    assert result.flagged_claims == []


def test_common_leading_words_are_not_flagged_as_claims():
    usecase = ValidateOutputUseCase()

    result = usecase.execute(
        output="The candidate is available immediately.",
        source_context="Ana is available immediately.",
    )

    assert "The" not in result.flagged_claims
