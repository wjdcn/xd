import streamlit as st

st.title("숫자 비율 계산기")

st.write("숫자를 입력하고 각 숫자의 전체 대비 비율을 확인하세요.")

# 숫자 입력 받기
numbers_input = st.text_area("숫자 목록을 입력하세요 (쉼표 또는 줄바꿈으로 구분)", "10, 20, 30")

# 입력 처리
def parse_numbers(text):
    # 쉼표 또는 줄바꿈 기준으로 분리
    parts = [p.strip() for p in text.replace('\n', ',').split(',')]
    try:
        return [float(p) for p in parts if p != '']
    except ValueError:
        return None

numbers = parse_numbers(numbers_input)

if numbers is None:
    st.error("숫자만 입력해주세요. 예: 10, 20, 30")
elif len(numbers) == 0:
    st.info("숫자를 입력하면 결과가 여기에 표시됩니다.")
else:
    total = sum(numbers)
    if total == 0:
        st.warning("합계가 0입니다. 비율을 계산할 수 없습니다.")
    else:
        st.subheader("결과")
        for i, num in enumerate(numbers):
            ratio = (num / total) * 100
            st.write(f"숫자 {num:.2f} → 비율: {ratio:.2f}%")
