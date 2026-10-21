-- 코드를 작성해주세요
-- 부서별 평균 연봉 조회
-- 부서별로 부서 ID, 영문 부서명, 평균 연봉 조회
-- 평균연봉은 소수점 첫째 자리에서 반올림하고 컬럼명은 AVG_SAL
-- 부서별 평균 연봉을 기준으로 내림차순

SELECT D.DEPT_ID, D.DEPT_NAME_EN, ROUND(AVG(E.SAL), 0) AS AVG_SAL
FROM HR_DEPARTMENT AS D
JOIN HR_EMPLOYEES AS E
ON D.DEPT_ID = E.DEPT_ID
GROUP BY D.DEPT_ID
ORDER BY AVG_SAL DESC;